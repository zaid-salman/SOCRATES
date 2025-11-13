import time
import controls_page
import day1

def menu():
    menu_input = input("\nGAMING\n\nOPTIONS: START (enter) CONTROLS (c) ")
    
    if menu_input != "c":
        welcome()
    else:
        controls_page.controls()
        menu()

def welcome():
    print("\nYou are a poor junior doctor at an underfunded and overworked hospital. You must use what little you remember from your binge drinking medical school days to treat as many patients as you can for you are DROWNING in student debt.")
    time.sleep(1)
    print("\nTo do so you must first ask a series of questions in the correct order, ask the correct follow up questions and prescribe/refer appropriately!")
    time.sleep(1)
    input("\nYou mustn't miss emergencies for they will result in... PATIENT DEATH. Be wary of tricky ethical dilemmas, flirtatious (but married) night shift staff and most importantly, YOUR STUDENT DEBT.\nPress enter to begin! ")

    day1.playday1()

menu()