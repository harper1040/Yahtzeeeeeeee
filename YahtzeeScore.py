"""
2024-10-27
Yahtzeee Score Criteria
"""
import YahtzeePlay as YP
import sys


def ChoiceNum(variables):     
    for i in variables["playdice"]:
        #print(i)
        if i == int(variables["scoreChoice"]):
            variables["foul"] += 1

    if variables["played"][variables["choice"][int(variables["scoreChoice"])]] == 1:
        print("No More Plays Available! Try Again!")
        variables["empty"] += 1
        return variables, False
    elif variables["foul"] == 0:
        print("You Fool You Don't Have Any of Those. Try Again!")
        variables["cheatTastic"] += 1
        return variables, False
    else:
        for i in variables["playdice"]:
            if i == int(variables["scoreChoice"]):
                variables["scoreDis"] += i
                variables["bonus"] += 1
        variables["played"][variables["choice"][int(variables["scoreChoice"])]] = 1 
        variables["playCount"] += 1  
        return variables, True
    
            
def ChoiceOther(variables):

    if variables["scoreChoice"] == "3o":
        if variables["played"]["3o"] == 1:
            print("No More Plays Available! Try Again!")
            variables["empty"] += 1
            return variables, False
        else:
            for n in range(1,7):
                value = variables["playdice"].count(n)
                if value == 3:
                    for f in variables["playdice"]:
                        variables["scoreDis"] += f
            variables["played"]["3o"] = 1
            variables["playCount"] += 1
            variables["foul"] += 1
            
        if variables["foul"] == 0:
            print("You Fool You Don't Have Any of Those. Try Again!")
            variables["cheatTastic"] += 1
            return variables, False
        return variables, True
                
    elif variables["scoreChoice"] == "4o":
        if variables["played"]["4o"] == 1:
            print("No More Plays Available! Try Again!")
            variables["empty"] += 1
            return variables, False
        else:
            for n in range(1,7):
                value = variables["playdice"].count(n)
                if value == 4:
                    for f in variables["playdice"]:
                        variables["scoreDis"] += f
            variables["played"]["4o"] = 1
            variables["playCount"] += 1
            variables["foul"] += 1
        if variables["foul"] == 0:
            print("You Fool You Don't Have Any of Those. Try Again!")
            variables["cheatTastic"] += 1
            return variables, False
        return variables, True
                
    elif variables["scoreChoice"] == "fh":
        fullHouse = 0
        if variables["played"]["fh"] == 1:
            print("No More Plays Available! Try Again!")
            variables["empty"] += 1
            return variables, False
        else:
            for n in range(1,7):
                three = (3*n)
                two = (2*n)
                value = variables["playdice"].count(n)
                if value == 3:
                    fullHouse += three
                    variables["foul"] += 3
                elif value == 2:
                    fullHouse += two
                    variables["foul"] += 2
        if fullHouse >= 7:
            variables["scoreDis"] += 25
            variables["played"]["fh"] = 1
            variables["playCount"] += 1
        if variables["foul"] < 5:
            print("You Fool You Don't Have Any of Those. Try Again!")
            variables["cheatTastic"] += 1
            return variables, False
        return variables, True

    elif variables["scoreChoice"] == "sl":
        slow = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
        if variables["played"]["sl"] == 1:
            print("No More Plays Available! Try Again!")
            variables["empty"] += 1
            return variables, False
        else:
            variables["playdice"].sort()
            set(variables["playdice"])
            order = 0
            for i in range(0,4):
                try:
                    if variables["playdice"][i] + 1 == variables["playdice"][i + 1]:
                        order += 1
                        
                except Exception:
                    IndexError
                    if variables["playdice"][i] + 1 == variables["playdice"][i]:
                        order += 1
            if order == 3:
                variables["scoreDis"] += 30
                variables["played"]["sl"] = 1
                variables["playCount"] += 1
            else:
                print("That's not a low straight!")
                variables["cheatTastic"] += 1
                return variables, False
            return variables, True

    elif variables["scoreChoice"] == "sh":
        shigh = [[2,3,4,5,6], [1,2,3,4,5]]
        if variables["played"]["sh"] == 1:
            print("No More Plays Available! Try Again!")
            variables["empty"] += 1
            return variables, False
        else:
            variables["playdice"].sort()
            if variables["playdice"] == shigh[0] or variables["playdice"] == shigh[1]:
                variables["scoreDis"] += 40
                variables["played"]["sh"] = 1
                variables["playCount"] += 1
            else:
                print("That's not a high straight!")
                variables["cheatTastic"] += 1
                return variables, False
            return variables, True

    elif variables["scoreChoice"] == "ch":
        if variables["played"]["ch"] == 2:
            print("No More Plays Available! Try Again!")
            variables["empty"] += 1
            return variables, False
        else:
            for i in variables["playdice"]:
                variables["scoreDis"] += i
        if variables["played"]["ch"] == 1:
            variables["played"]["ch"] = 2
            variables["playCount"] += 1 
        else:
            variables["played"]["ch"] = 1
        return variables, True       

    elif variables["scoreChoice"] == "yz":
        yahtzee = 0
        for n in range(1,7):
            yahtzee = variables["playdice"].count(n)
            if yahtzee == 5 and variables["played"]["yz"] > 0:
                variables["scoreDis"] += 100
                variables["played"]["yz"] += 1
                variables["foul"] += 1
                return variables, True 
            elif yahtzee == 5:
                variables["scoreDis"] += 50
                variables["played"]["yz"] += 1
                variables["foul"] += 1          
                return variables, True       
            
            if variables["foul"] == 0:
                print("Sorry That's not a Yahtzeeeeee!")
                return variables, False    
                

def Score(variables):
    diceCount = 0    
    
#Check for cheating or lack of playable rolls.
    while True:
        if variables["cheatTastic"] == 3:
            print("Shame on You for Trying to Cheat, I End Your Game! You Dissapoint Me!!")
            sys.exit(0)
        if variables["empty"] == 3:
                print("You don't seems to have any more plays")
                print(f"You scored " + YP.escape.GREEN + str(variables["scoreDis"]) + YP.escape.END + " points!")
                print("Thanks For Playing!!")
                sys.exit(0)
        for num in range(1,7):
            if variables["playdice"].count(num) != 5:
                diceCount += 1
        if diceCount == 6 and variables["playCount"] == 12: 
            print(f"Game Over! You Scored: {variables["scoreDis"]}, and you got {variables["played"]['yz']} Yahtzeeeeee's")
            variables["gameBegan"] = 2
            sys.exit(0)
        
        variables["scoreChoice"] = input(f"""
        You are out of rolls how would you like to play your dice?
            (1)'s (2)'s (3)'s (4)'s (5)'s (6)'s
            (3o)f a Kind (that's the letter o)
            (4o)f a Kind (that's the letter o)
            (fh)Full House (that's 2 of one and thee of another)
            (sl)Straight Low 
            (sh)Straight High 
            (ch)Chance you can literally play anything and can choose this two times.
            (yz)YAHTZEE!!!
            
                            {variables["playdice"]}
    \n""").lower()

    #Scoring Logic check for user input for what they want to play and then verify the dice are there then payout.
        try: 
            int(variables["scoreChoice"])
            variables, leave = ChoiceNum(variables)  
            
        except:
            variables, leave = ChoiceOther(variables)  

        if leave:
            variables["turns"] = 0
            variables["foul"] = 0

            if variables["bonus"] >= 63 and variables["played"]["bo"] == 0:
                variables["scoreDis"] += 35
                variables["played"]["bo"] = 1
                input("You got the BONUS!!")
            return variables
        
