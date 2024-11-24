"""
2024-10-27
Game File Yahtzeeeee
"""
import time
import random
import YahtzeeScore as YS
import os


class escape:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CLEAR ='\x1b[2K'
   UP ='\033[1A'

def ClearScreen():
    """Clears terminal screen"""
    try:
        os.system('clear')
    except:
        os.system('cls')

def ScoreBoard(variables):
    print("\n          \\/Hands you have played\\/", "Your score is: " + escape.BLUE + str(variables["scoreDis"]) + escape.END)
    print(Used(variables))

def NewGame(variables):
    SKIP_LIST = ["played", "choice"]
    for i in variables:
        if i == "holdem" or i == "scoreChoice":
            variables[i] = ""
        elif i in SKIP_LIST:
            pass
        else:
            variables[i] = 0
    for i in variables["played"]:
        variables["played"][i] = 0
    return variables

def GameLoop(variables):
    ClearScreen()
    ScoreBoard(variables)
    variables["playdice"] = Roll()
    variables, winCheck = Hold(variables)
    if winCheck:
        return variables
    ClearScreen()
    ScoreBoard(variables)
    variables["playdice"] = SubRoll(variables)
    variables, winCheck = Hold(variables)
    if winCheck:
        return variables
    ClearScreen()
    ScoreBoard(variables)
    variables["playdice"] = SubRoll(variables)
    variables = YS.Score(variables)
    ClearScreen()
    return variables
    
    
def Roll():
    roll = []
    for i in range(1,6):
        dieRoll = random.randint(1,6)
        roll.append(dieRoll)
    return roll
      
    

def Used(variables):
    list = []
    for i in variables["played"]:
        if variables["played"][i] == "ch" and "ch" > 2:
            list.append(i)
        if variables["played"][i] > 0 and variables["played"][i] != "ch":
            list.append(i)
    return list

def SubRoll(variables):
    subDice = []
    counter = 0
    for i in variables["holdem"]:
        if i == "H":
            subDice.append(variables["playdice"][counter])
        elif i == "R":
            dieRoll = random.randint(1,6)
            subDice.append(dieRoll)
        counter += 1
        
    return subDice

# This Func takes your initial die roll and prompts you to hold any you want and then puts you though another roll and then scoring.
def Hold(variables):

    while True:
        counter = 0
        HOLD_VALID = ["H", "R"]

        if variables["turns"] == 2:
            variables = YS.Score(variables)
            return variables, True  
    
        #print("\n          \\/Hands you have played\\/", "Your score is: " + escape.BLUE + str(variables["scoreDis"]) + escape.END)        
        #print(used())
        variables["holdem"] = input(f"""
        Please choose to hold dice or roll again.
        Enter an R to roll and H to hold for each die. ex. HRRHR    
                    {variables["playdice"]}
                 """).upper()
        if variables["holdem"] == "Q":
            variables["gameBegan"] = 3
            return variables, True
        #Checks to make sure you didn't put in 6 inputs and chose what to do with all your dice.
        elif len(variables["holdem"]) >= 6 or len(variables["holdem"]) <= 4 and variables["turns"] != 3:
            print("I don't think you understood make 5 inputs no spaces R and H only.")
        else:
            for i in variables["holdem"]:
                if i in HOLD_VALID:
                    counter +=1
                else:
                    print("Wrong Value Only Use H or R please")
            if counter == 5:
                break
    variables["turns"] += 1
    if variables["holdem"] == "HHHHH":
        variables = YS.Score(variables)
        return variables, True 
    return variables, False
    
    
