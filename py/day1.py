import time
import variables
import formatting
import patient

def playday1():
    print("\n\nDAY 1:")
    time.sleep(2)

    player_name = input(f"\n{formatting.get_balls()}: YEEEEEOOOOOOOWWWWWWHHHH MY BALLLLLLSSS THEY TOOK MY BALLSSS\n{formatting.get_yang()}: CAN SOMEONE PLEASE GET BALLS GUY SOME OPIOIDS - anyways, hi there I'm Dr Yang, what was your name again?\nInput name: ")

    variables.write_json("player_name", player_name)

    print(f"\n{formatting.get_yang()}: Well {player_name}, it's great to have you on board, we've always needed doctors like you, so young and naive! hahaha\n{formatting.get_yang()}: ... I'm going to need you to see our... Ahem lovely line of patients. I will be very busy seeing the nur- important patients so I do not think I will be around as much as I'd like. I hope that this book can serve as a guide for you.\n")
    time.sleep(3)

    input("\n\033[91m\x1B[3mYOU HAVE RECEIVED THE RED BOOK! PRESS 'r' WHENEVER YOU NEED TO REFER TO IT.\x1B[0m\033[00m\nPress enter to continue. ")
    
    input(f"\n{formatting.get_yang()}: For now, just give me the diagnosis of each patient, no need to prescribe just yet. NEVER MISS AN EMERGENCY - anyone who comes in with a '{formatting.red_italic("THUNDERCLAP HEADACHE")}' or '{formatting.red_italic("CRUSHING CHEST PAIN")}' or '{formatting.red_italic("DROOPING FACE AND ARM")}' must IMMEDIATELY be reported by pressing '!'\n{formatting.get_yang()}: Otherwise follow the structure of\n(1) {formatting.red_italic("PRESENTING COMPLAINT")}\n(2) {formatting.red_italic("HISTORY OF PRESENTING COMPLAINT")}\n(3) {formatting.red_italic("PAST MEDICAL HISTORY")}\n(4) {formatting.red_italic("MEDICATION HISTORY")}\n(5) {formatting.red_italic("SOCIAL HISTORY")}\n(6) {formatting.red_italic("FAMILY HISTORY")}\n...ALWAYS IN THAT ORDER!\nPress enter to continue. ")

    input(f"\n{formatting.get_yang()}: You can take a history of presenting complaint by using the acronym SOCRATES to help you out:\n{formatting.red_italic("SITE")} (where is it),\n{formatting.red_italic("ONSET")} (when did it start),\n{formatting.red_italic("CHARACTERISTICS")} (What does the pain feel like),\n{formatting.red_italic("RADIATION")} (does the pain move?),\n{formatting.red_italic("ASSOCIATED SYMPTOMS")},\n{formatting.red_italic("TIMING")} (is it constant or does it come and go),\n{formatting.red_italic("EXACERBATING/ALLEVIATING FACTORS")} (what makes it better or worse),\n{formatting.red_italic("SEVERITY")} (scale of 1-10)\nPress enter to continue. ")

    print(f"\n{formatting.get_yang()}: ahem... don't tell anyone but because we are so short on time, it's okay if you skip some questions AS LONG AS THE DIAGNOSIS IS CORRECT and that you HAVEN'T MISSED ANY CRUCIAL INFO.\n{formatting.get_yang()}: For today... it looks like we've just got some {formatting.red_italic("ASTHMA")} patients, patients with {formatting.red_italic("HEADACHES")}, some {formatting.red_italic("BROKEN BONES")}, and colds. Some people may just be here because they want to chat - you can just {formatting.red_italic("SKIP")} or {formatting.red_italic("INTERRUPT")} them if they are going on and on for too long. But of course don't be too rude otherwise you'll get a reputation.")

    patient.first_conversation("bob", f"Hi, how are you!\n\n{formatting.get_player()}: Good, thank you!")