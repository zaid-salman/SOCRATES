import variables

def get_player():
    player_name = variables.read_json("player_name")
    return f"\033[91m{player_name}\033[0m"

def get_patient(name):
    return f"\033[34m{name.capitalize()}\033[0m"

def get_yang():
    return "\033[95mDr. Yang\033[0m"

def get_balls():
    return "\033[94mBalls Guy\033[0m"

def red_italic(text):
    return f"\033[91m\x1B[3m{text}\x1B[0m\033[0m"