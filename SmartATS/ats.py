import json
import re
from SmartATS.readtext import readText
import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from SmartATS.readtext import readText
from SmartATS.createpf import createPortfolio


# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Example text from the PDF conversion
resume_text = readText('resume.pdf')

def split_sections(text):
    section_headers = [
        'Education', 'Experience', 'Projects', 'Skills', 'Contact Information',
        'Technical Skills', 'Languages and Tech Stack', 'Personal Projects', 'Position of Responsibility'
    ]
    section_pattern = re.compile(r'|'.join(rf'\b{header}\b' for header in section_headers), re.IGNORECASE)

    sections = {header: [] for header in section_headers}
    current_section = None

    for line in text.split('\n'):
        line = line.strip()
        match = section_pattern.match(line)
        if match:
            current_section = match.group(0).strip()
        elif current_section:
            sections[current_section].append(line)

    return sections

def clean_section_data(section_data):
    cleaned_data = []
    for line in section_data:
        clean_line = line.strip()
        if clean_line and not clean_line.isspace():
            cleaned_data.append(clean_line)
    return cleaned_data

def parse_resume(resume_text):
    if not isinstance(resume_text, str):
        raise ValueError("The resume text must be a string.")
    
    sections = split_sections(resume_text)
    
    for section in sections:
        sections[section] = clean_section_data(sections[section])
    
    return sections

def create_candidate_profile(parsed_data):
    profile = {
        "education": parsed_data.get("Education", []),
        "experience": parsed_data.get("Experience", []),
        "projects": parsed_data.get("Projects", []) + parsed_data.get("Personal Projects", []),
        "skills": parsed_data.get("Skills", []) + parsed_data.get("Technical Skills", []) + parsed_data.get("Languages and Tech Stack", []),
        "contact_info": parsed_data.get("Contact Information", []),
        "positions_of_responsibility": parsed_data.get("Position of Responsibility", [])
    }
    return profile


# Parse the resume
parsed_resume = parse_resume(resume_text)

temp_portfolio = json.dumps(parsed_resume, indent=4)



candidatePortfolio = createPortfolio(temp_portfolio)
