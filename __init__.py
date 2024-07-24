import PyPDF2
import random
import re
from pathlib import Path

# Path to the PDF file in Google Drive
pdf_path = Path(__file__).with_name('SampleSet.pdf')

def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    text = ''
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    return text

def parse_quizbowl_problems(text):
    problems = re.split(r'\d+:\s', text)[1:]  # Split and remove the first empty part
    formatted_problems = []
    for problem in problems:
        toss_up_match = re.search(r'^(.*?)\nB1:', problem, re.DOTALL)
        bonus1_match = re.search(r'B1:\s(.*?)\nB2:', problem, re.DOTALL)
        bonus2_match = re.search(r'B2:\s(.*?)(?:\n|$)', problem, re.DOTALL)

        if toss_up_match and bonus1_match and bonus2_match:
            toss_up = toss_up_match.group(1)
            bonus1 = bonus1_match.group(1)
            bonus2 = bonus2_match.group(1)

            # Remove answers in uppercase
            toss_up = re.sub(r'\b[A-Z]+\b', '', toss_up)
            bonus1 = re.sub(r'\b[A-Z]+\b', '', bonus1)
            bonus2 = re.sub(r'\b[A-Z]+\b', '', bonus2)

            formatted_problems.append({
                'toss_up': toss_up.strip(),
                'bonus1': bonus1.strip(),
                'bonus2': bonus2.strip()
            })
    return formatted_problems

def quizbowl_session(problems):
    problem = random.choice(problems)
    print("Toss-Up Question:")
    print(problem['toss_up'])
    input("Your answer: ")
    toss_up_answer = re.search(r'\b[A-Z]+\b', problem['toss_up'])
    if toss_up_answer:
        print("Correct answer:", toss_up_answer.group(0))

    print("\nBonus Question 1:")
    print(problem['bonus1'])
    input("Your answer: ")
    bonus1_answer = re.search(r'\b[A-Z]+\b', problem['bonus1'])
    if bonus1_answer:
        print("Correct answer:", bonus1_answer.group(0))

    print("\nBonus Question 2:")
    print(problem['bonus2'])
    input("Your answer: ")
    bonus2_answer = re.search(r'\b[A-Z]+\b', problem['bonus2'])
    if bonus2_answer:
        print("Correct answer:", bonus2_answer.group(0))

# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_path)
print(pdf_text)

# Parse Quizbowl problems
quizbowl_problems = parse_quizbowl_problems(pdf_text)

# Start a Quizbowl session
quizbowl_session(quizbowl_problems)