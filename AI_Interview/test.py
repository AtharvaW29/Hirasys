from langchain_community.llms import Ollama
import speech_recognition as sr
import whisper
import numpy as np
import time
import torch
import pyttsx3
from extract_SW import add_strengths_and_weaknesses_to_portfolio
# Initialize interview data dictionary
interview_data = {}

def store_interview(question, answer):
    """Store question and answer in interview_data dictionary."""
    global interview_data
    interview_data[question] = answer

engine = pyttsx3.init()           
engine.setProperty('rate', 160)  
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def analyze_strengths_and_weaknesses(interview_data, llm_model):
    

        # Define prompts based on the question and expected responses
        prompt = f"Identify strengths and weaknesses in the candidate's interview based on the confidence and detailness of the answers, Give me strengths and weaknesses in points like, Strengths: , Weaknesses: , Here is the interview dictionary with questions and its answers {interview_data}\n"

        # Use Llama3 to generate responses based on prompts
        response = llm_model.invoke(prompt)

        # Analyze Llama3 generated responses to determine strengths and weaknesses
        return response

def audio_to_numpy(audio_data):
    """Convert AudioData to numpy array."""
    audio_bytes = audio_data.get_raw_data()
    audio_np = np.frombuffer(audio_bytes, dtype=np.int16)
    audio_np = audio_np.astype(np.float32) / 32768.0  # Normalize audio
    return audio_np

def resample_audio(audio_np, original_rate=44100, target_rate=16000):
    """Resample the audio numpy array to the target rate."""
    audio_tensor = torch.from_numpy(audio_np).unsqueeze(0).unsqueeze(0)  # Shape (1, 1, length)
    resampled_audio = torch.nn.functional.interpolate(audio_tensor, scale_factor=target_rate/original_rate, mode='linear', align_corners=False)
    return resampled_audio.squeeze().numpy()

def speech_to_text(model):
    """Transcribe speech to text using Whisper model."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your answer...")
        audio_data = recognizer.listen(source)

    audio_np = audio_to_numpy(audio_data)  # Convert audio to numpy array
    audio_np = audio_np.flatten()  # Flatten numpy array
    resampled_audio = resample_audio(audio_np)  # Resample audio to 16000 Hz

    result = model.transcribe(resampled_audio)  # Transcribe using Whisper
    text = result['text']
    print(f"Recognized text: {text}")
    return text

def generate_follow_up(question, answer, model):
    """Generate follow-up question and retrieve answer using Llama3."""
    prompt = (
        f"Act like an interviewer and ask questions based on the candidate's response to get to know more about it in detail and only ask questions, Here is the question asked and the response given by them .Interviewer: {question}\nCandidate: {answer}\n"
        f"Now ask a single question based on the response to test how much the candidate actually knows!"
    )
    follow_up = model.invoke(prompt)
    engine.say(follow_up)
    engine.runAndWait()
    return follow_up

def interview_module():
    """Main function to conduct the interview process."""
    llm = Ollama(model="llama3")
    whisper_model = whisper.load_model("base")
    questions = [
        "Can you tell me about yourself?",
        # "Why do you want to work for our company?",
        # "What are your strengths and weaknesses?",
        # "Can you describe a challenging situation and how you handled it?"
    ]
    
    for question in questions:
        print(f"Question: {question}")
        answer = None
        while not answer:  # Keep listening until valid answer is received
            answer = speech_to_text(whisper_model)
        store_interview(question, answer)

        # Generate follow-up question and retrieve answer
        follow_up_question = generate_follow_up(question, answer, llm)
        time.sleep(8)
        
        # Ask for follow-up answer
        follow_up_answer = None
        while not follow_up_answer:  # Keep listening until valid follow-up answer is received
            follow_up_answer = speech_to_text(whisper_model)
        
        store_interview(follow_up_question, follow_up_answer)

        # Generate and retrieve the next follow-up question
        # follow_up_question = generate_follow_up(follow_up_question, follow_up_answer, llm)
        # time.sleep(8)

        # # Ask for follow-up answer
        # follow_up_answer = None
        # while not follow_up_answer:  # Keep listening until valid follow-up answer is received
        #     follow_up_answer = speech_to_text(whisper_model)
        
        # store_interview(follow_up_question, follow_up_answer)
        print("Moving on to the next main question...\n")
    
    # After all questions are answered, analyze strengths and weaknesses
    strengths_weaknesses_analysis = analyze_strengths_and_weaknesses(interview_data, llm)
    print("Strengths and Weaknesses Analysis:")
    print(strengths_weaknesses_analysis)
    
    portfolio_file = 'D:\Hirasys_AI\portfolio.json'
    add_strengths_and_weaknesses_to_portfolio(portfolio_file, strengths_weaknesses_analysis)
if __name__ == "__main__":
    interview_module()
