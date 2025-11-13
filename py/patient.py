import random
import formatting

intro_quips = ["Can you guys please hurry up, we're just about dying waiting for you", "... The lines long isn't it", "finally... hi", "...", "Hello", "Greetings good sir", "Yo doc", "Hi", "\x1B[3msigh...\x1B[0m hi,", "\x1B[3mcough cough\x1B[0m hi doc"]

def intro(name, intro_text):
    print(formatting.get_patient(name) + ": " + intro_text)

def first_conversation(name, intro_text):
    standard_conversation(name, intro_text)

def standard_conversation(name="Patient", intro_text=None):
    intro(name, intro_text)

    questions = ["Presenting Complaint", "History of Presenting Complaint", "Past Medical History", "Past Medication History", "Family History", "Social History"]
    random.shuffle(questions)

    for i in range(1, 7):
        print(questions[i - 1] + f" ({i})")
    
    q1 = input(f"\nInput number to choose questions in the correct order, one at a time. ")