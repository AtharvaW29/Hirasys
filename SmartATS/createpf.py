import json
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

output_file = "portfolio.json"
def createPortfolio(temp_portfolio):
    prompt = (
        f"This is the Candidate's resume in JSON format, i want you to clean it a lot so that the output you will give can be used to update it constantly via JSON Api calls, I want you to only give the output i dont want any unnecessary details like 'here is the cleaned up version etc etc', heres the resume: {temp_portfolio} \n"
    )
    follow_up = llm.stream(prompt)
    json_data = ""
    started = False
    
    for chunk in follow_up:
        print(chunk, end = "", flush = True)
        if "{" in chunk:
            started = True
        if started:
            json_data += chunk


    with open(output_file, 'w') as f:
            
            f.write(json_data)
   
        