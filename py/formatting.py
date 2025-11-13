player = ""

def get_player():
    return "\033[91m{player}\033[0m"

def get_patient():
    return "\033[34mPatient\033[0m"

def get_yang():
    return "\033[95mDr. Yang\033[0m"

def get_balls():
    return "\033[94mBalls Guy\033[0m"

def set_player(name):
    player = name

def red_italic(text):
    return "\033[91m\x1B[3m{text}\x1B[0m\033[0m"