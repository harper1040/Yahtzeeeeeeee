"""
Joey Harper
Yahtzee!!
2024-09-10
"""

import time
import random


turns = 0
scoreDis = 0
holdem = "" 
playCount = 0
cheatTastic = 0
played = {"one":0, "two":0, "three":0, "four":0, "five":0, "six":0, "fh":0, "yz":0, "4o":0, "3o":0, "sh":0, "sl":0, "ch":0}
foul = 0
empty = 0

gameBegan = 0

def newGame():
    global cheatTastic
    global foul
    global empty
    foul = 0
    empty = 0
    scoreDis = 0
    playCount = 0
    for i in played:
        played[i] = 0
    #print(scoreDis, playCount, played)

def gameLoop():
    global turns
    global playCount
    turns = 0
    playDice = []
    
    
    def start():
        global holdem
        global played

        for i in range(1,6):
            dieRoll = random.randint(1,6)
            playDice.append(dieRoll)
        hold(playDice)   

    def used():
        list = []
        for i in played:
            if played[i] == "ch" and "ch" > 2:
                list.append(i)
            if played[i] > 0 and played[i] != "ch":
                list.append(i)
        return list

    def subRoll(dice, hold):
        subDice = []
        counter = 0
        for i in hold:
            if i == "H":
                subDice.append(dice[counter])
            elif i == "R":
                dieRoll = random.randint(1,6)
                subDice.append(dieRoll)
            counter += 1
            
        return subDice

    def score(dice):
        global scoreDis
        global playCount
        global gameBegan
        global cheatTastic
        global empty
        global foul
        diceCount = 0
        
    #Check for cheating or lack of playable rolls.
        if cheatTastic == 3:
            return
        if empty == 3:
                print("You don't seems to have any more plays")
                print(f"You scored {scoreDis} points!")
                print("Thanks For Playing!!")
                gameBegan = 2
                return
        for num in range(1,7):
            if dice.count(num) != 5:
                diceCount += 1
        if diceCount == 6 and playCount == 11: 
            print(f"Game Over! You Scored: {scoreDis}, and you got {played['yz']} Yahtzeeeeee's")
            gameBegan = 2
            return
        
        userChoice= input(f"""
        You are out of rolls how would you like to play your dice?
            (1)'s (2)'s (3)'s (4)'s (5)'s (6)'s
            (3o)f a Kind (that's the letter o)
            (4o)f a Kind (that's the letter o)
            (fh)Full House (that's 2 of one and thee of another)
            (sl)Straight Low 
            (sh)Straight High 
            (ch)Chance you can literally play anything and can choose this two times.
            (yz)YAHTZEE!!!
            
                          {dice}
    \n""").lower()
    
    #Scoring Logic check for user input for what they want to play and then verify the dice are there then payout.
        if userChoice == "1":
            for i in dice:
                if i == 1:
                    foul += 1
            if played["one"] == 1:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            elif foul == 0:
                print("You Fool You Don't Have Any of Those. Try Again!")
                cheatTastic += 1
                score(dice)
            else:
                for i in dice:
                    if i == int(userChoice):
                        scoreDis += i
                played["one"] = 1 
                playCount += 1
                print(scoreDis)            
        
        elif userChoice == "2":
            for i in dice:
                if i == 2:
                    foul += 1
            if played["two"] == 1:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            elif foul == 0:
                print("You Fool You Don't Have Any of Those. Try Again!")
                cheatTastic += 1
                score(dice)
            else:
                for i in dice:
                    if i == int(userChoice):
                        scoreDis += i
                played["two"] = 1 
                playCount += 1 
        
        elif userChoice == "3":
            for i in dice:
                if i == 3:
                    foul += 1
            if played["three"] == 1:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            elif foul == 0:
                print("You Fool You Don't Have Any of Those. Try Again!")
                cheatTastic += 1
                score(dice)
            else:
                for i in dice:
                    if i == int(userChoice):
                        scoreDis += i
                played["three"] = 1 
                playCount += 1 
        
        elif userChoice == "4":
            for i in dice:
                if i == 4:
                    foul += 1
            if played["four"] == 1:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            elif foul == 0:
                print("You Fool You Don't Have Any of Those. Try Again!")
                cheatTastic += 1
                score(dice)
            else:
                for i in dice:
                    if i == int(userChoice):
                        scoreDis += i
                played["four"] = 1 
                playCount += 1 
        
        elif userChoice == "5":
            for i in dice:
                if i == 5:
                    foul += 1
            if played["five"] == 1:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            elif foul == 0:
                print("You Fool You Don't Have Any of Those. Try Again!")
                cheatTastic += 1
                score(dice)
            else:
                for i in dice:
                    if i == int(userChoice):
                        scoreDis += i
                played["five"] = 1 
                playCount += 1 

        elif userChoice == "6":
            for i in dice:
                if i == 6:
                    foul += 1
            if played["six"] == 1:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            elif foul == 0:
                print("You Fool You Don't Have Any of Those. Try Again!")
                cheatTastic += 1
                score(dice)
            else:
                for i in dice:
                    if i == int(userChoice):
                        scoreDis += i
                played["six"] = 1 
                playCount += 1 

        elif userChoice == "3o":
            if played["3o"] == 1:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            else:
                for n in range(1,7):
                    value = dice.count(n)
                    if value == 3:
                        scoreDis += n * 3
                        played["3o"] = 1
                        playCount += 1
                        foul += 1
            if foul == 0:
                print("You Fool You Don't Have Any of Those. Try Again!")
                cheatTastic += 1
                score(dice)
                    
        elif userChoice == "4o":
            if played["4o"] == 1:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            else:
                for n in range(1,7):
                    value = dice.count(n)
                    if value == 4:
                        scoreDis += n * 4
                        played["4o"] = 1
                        playCount += 1
                        foul += 1
            if foul == 0:
                print("You Fool You Don't Have Any of Those. Try Again!")
                cheatTastic += 1
                score(dice)
                    
        elif userChoice == "fh":
            fullHouse = 0
            if played["fh"] == 1:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            else:
                for n in range(1,7):
                    three = (3*n)
                    two = (2*n)
                    value = dice.count(n)
                    if value == 3:
                        fullHouse += three
                        foul += 3
                    elif value == 2:
                        fullHouse += two
                        foul += 2
            if fullHouse >= 7:
                scoreDis += 25
                played["fh"] = 1
                playCount += 1
            if foul < 5:
                print("You Fool You Don't Have Any of Those. Try Again!")
                cheatTastic += 1
                score(dice)

        elif userChoice == "sl":
            slow = [1,2,3,4,5]
            if played["sl"] == 1:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            else:
                dice.sort()
                if dice == slow:
                    scoreDis += 30
                    played["sl"] = 1
                    playCount += 1
                else:
                    print("That's not a low straight!")
                    cheatTastic += 1

        elif userChoice == "sh":
            shigh = [2,3,4,5,6]
            if played["sh"] == 1:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            else:
                dice.sort()
                if dice == shigh:
                    scoreDis += 40
                    played["sh"] = 1
                    playCount += 1
                else:
                    print("That's not a high straight!")
                    cheatTastic += 1

        elif userChoice == "ch":
            if played["ch"] == 2:
                print("No More Plays Available! Try Again!")
                empty += 1
                score(dice)
            else:
                for i in dice:
                    scoreDis += i
                played["ch"] = 1
                playCount += 1            

        elif userChoice == "yz":
            yahtzee = 0
            for n in range(1,7):
                yahtzee = dice.count(n)
                if yahtzee == 5 and played["yz"] > 0:
                    scoreDis += 100
                    played["yz"] += 1
                    foul += 1
                elif yahtzee == 5:
                    scoreDis += 50
                    played["yz"] += 1
                    foul += 1                
                    
            if foul == 0:
                print("You Fool You Don't Have Any of Those. Try Again!")
                cheatTastic += 1
                score(dice)

        #print(f"play count {playCount}")        
        #print(f"\nYour score {scoreDis}\n")
            

# This Func takes your initial die roll and prompts you to hold any you want and then puts you though another roll and then scoring.
    def hold(playDice):
        global turns
        global holdem
        global gameBegan

        print("          \\/Hands you have played\\/", f"Your score is: {scoreDis}")        
        print(used())
        holdem = input(f"""
        Please choose to hold dice or roll again.
        Enter an R to roll and H to hold for each die. ex. HRRHR    
                    {playDice}
                 """).upper()
        if holdem == "Q":
            gameBegan = 3
            return
        #Checks to make sure you put in 6 inputs and chose what to do with all your dice.
        elif len(holdem) >= 6 or len(holdem) <= 4:
            print("Don't think you understood make 5 inputs no spaces R and H only.")
            hold(playDice)

        for i in holdem:
            if i == "H" or i == "R":
                pass
            else:
                print("Wrong Value Only Use H or R please")
                hold(playDice)
        turns += 1
        if holdem == "HHHHH":
            score(playDice)
            return
        elif turns == 3:
            score(playDice)
            return        
        
        playDice = subRoll(playDice, holdem)
               
        hold(playDice)
    
    # For loop to get initial die roll
    
    start()
        
    
#The starting loop to check if the player wants to.... play.
while True:
    if cheatTastic == 3:
        print("Shame on You I End Your Game! You Dissapoint Me!!")
        cheatTastic = 0
        break
    if gameBegan == 0:
        roll = input("""
        Hello and Welcome to Yahtzeeeeeeeee!! All Those E's Assure You This is it's Own Unique Game ;)
        Choose what you would like to do:
        (P)lay
        (Q)uit
        """).upper()
    elif gameBegan == 1:
        roll = input("""
        Choose what you would like to do:
        (P)lay On
        (Q)uit
        """).upper()
    elif gameBegan == 2:
        roll = input("""
        Good Game if you wanna play again choose:
        (N)ew Game or
        (Q)uit
""").upper()
    elif gameBegan == 3:
        break
    gameBegan = 0

    if roll == "P":
        gameLoop()
        if gameBegan == 0:
            gameBegan = 1
        elif gameBegan == 2:
            pass
    elif roll == "Q":
        print("\nYou make me sad!")
        break
    elif roll == "N":
        #print(scoreDis, playCount, played)
        newGame()
    else:
        print("ERROR, ERROR!! But of course you knew that make a proper selection, this isn't yutzee!")
        gameBegan = 1