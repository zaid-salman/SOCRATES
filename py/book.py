book = {"Presenting Complaint": "What brings you in today?",
        "History of Presenting Complaint": "SOCRATES\n\tWhere is it?\n\tWhen did it start?\n\tWhat would you describe the pain as?\n\tDoes the pain move or radiate?\n\tAre there any associated symptoms?\n\tHow long have you had this pain, does the pain come and go? When is it worse?\n\tHas the pain gotten better or worse and is there anything that makes pain better or worse?\n\tHow would you rate the severity of the pain?",
        "Past Medical History": "Do you have any other medical conditions that you're aware of?\nHas there been anything else that you've seen your GP for?\nDo you have any allergies?",
        "Past Medication History": "Are you on any medications at the moment? If so, what are they?",
        "Family History": "Do you have anything that runs in the family?",
        "Social History": "Standard lifestyle questions that we ask for everyone - smoking, drinking, drugs.\nWhat do you do for work? Where have you worked in the past?\nDo you live with anyone at home?",
        "Emergencies": "",
        "Asthma": "Risk Factors: non-modifiable (atopy, male sex for development, female sex for persistence, prematurity); modifiable (smoking, obesity, infections, social deprivation).\nSymptoms: diurnal wheeze, cough, breathlessness; exacerbated by triggers (pets, dust, cold air, occupation); assess exacerbation history and adherence to treatment.",
        "Common Cold": "Symptoms: sneezing, runny nose, stuffy nose, cough, no fever"}

keys = {"pc": "Presenting Complaint",
        "hpc": "History of Presenting Complaint",
        "pmh": "Past Medical History",
        "pmx": "Past Medication History",
        "fh": "Family History",
        "sh": "Social History",
        "e": "Emergencies",
        "asthma": "Asthma",
        "cold": "Common Cold"}

def open_book(book):
    for key in book.keys():
        print(f"\033[91m{key}\033[00m: {book[key]}")

def open_key(key):
    section = keys[key]
    print(f"\033[91m{section}\033[00m: {book[section]}")