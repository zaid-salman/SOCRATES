def open_book(red_book):
    print(f"\033[91m{red_book}\033[00m")

book = {"pc": "What brings you in today?",
        "hpc": "SOCRATES\nWhere is it?\nWhen did it start?\nWhat would you describe the pain as?\nDoes the pain move or radiate?\nAre there any associated symptoms?\nHow long have you had this pain, does the pain come and go? When is it worse?\nHas the pain gotten better or worse and is there anything that makes pain better or worse?\nHow would you rate the severity of the pain?",
        "pmh": "Do you have any other medical conditions that you're aware of?\nHas there been anything else that you've seen your GP for?\nAre you on any medications at the moment? If so, what are they?\nDo you have any allergies?",
        "sh": "Standard lifestyle questions that we ask for everyone - smoking, drinking, drugs.\nWhat do you do for work? Where have you worked in the past?\nDo you live with anyone at home?",
        "fh": "Do you have anything that runs in the family?"}