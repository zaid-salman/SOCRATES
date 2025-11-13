import json

def read_json(var):
    with open("variables.json", "r") as var_file:
        variables = json.load(var_file)
    return variables[var]

def write_json(var, value):
    with open("variables.json", "r") as var_file:
        variables = json.load(var_file)
    
    variables[var] = value
    
    with open("variables.json", "w") as var_file:
        json.dump(variables, var_file)