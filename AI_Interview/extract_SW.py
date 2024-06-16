import json

def extract_strengths_and_weaknesses(text):
    # Assuming text contains both strengths and weaknesses in a specific format
    strengths_section = text.split("**Strengths:**")[1].split("**Weaknesses:**")[0].strip()
    weaknesses_section = text.split("**Weaknesses:**")[1].strip()
    
    strengths = [s.strip() for s in strengths_section.split('\n') if s.strip()]
    weaknesses = [w.strip() for w in weaknesses_section.split('\n') if w.strip()]
    
    return strengths, weaknesses

def add_strengths_and_weaknesses_to_portfolio(portfolio_file, interview_output):
    # Load the existing portfolio JSON data
    with open(portfolio_file, 'r') as file:
        portfolio_data = json.load(file)

    # Extract and format strengths and weaknesses from interview output
    strengths, weaknesses = extract_strengths_and_weaknesses(interview_output)

    # Add strengths and weaknesses to the portfolio data
    portfolio_data["Strengths"] = strengths
    portfolio_data["Weaknesses"] = weaknesses

    # Save the updated portfolio back to a JSON file
    updated_output_file = "portfolio.json"
    with open(updated_output_file, 'w') as file:
        json.dump(portfolio_data, file, indent=2)

    print(f"Updated portfolio saved to {updated_output_file}")