"""
2024-10-27
Yahtzeeeee Fixed 
"""
import YahtzeePlay as YP

gameVars = {"turns": 0, "scoreDis": 0, "playCount": 0, "holdem": "", "cheatTastic": 0, "foul": 0, "empty": 0, "bonus": 0, "gameBegan": 0, "scoreChoice": "", "playdice": [],
            "played" :{"one":0, "two":0, "three":0, "four":0, "five":0, "six":0, "fh":0, "yz":0, "4o":0, "3o":0, "sh":0, "sl":0, "ch":0, "bo":0},
            "choice" :{1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", "fh":0, "yz":0, "4o":0, "3o":0, "sh":0, "sl":0, "ch":0, "bo":0}}

def main(variables):
    #The starting loop to check if the player wants to.... play.
    while True:

        if variables["gameBegan"] == 0:
            roll = input("""\n
            Hello and Welcome to Yahtzeeeeeeeee!! All Those E's Assure You This is it's Own Unique Game ;)
            Choose what you would like to do:
            (P)lay
            (Q)uit
            """).upper()
        elif variables["gameBegan"] == 1:
            roll = input("""\n
            Choose what you would like to do:
            (P)lay On
            (Q)uit
            """).upper()
        elif variables["gameBegan"] == 2:
            roll = input("""\n
            Good Game if you wanna play again choose:
            (N)ew Game or
            (Q)uit
        """).upper()
        elif variables["gameBegan"] == 3:
            YP.ClearScreen()
            print("\nGood Game your score Was: " + YP.escape.GREEN + str(variables["scoreDis"]) + YP.escape.END + "You got " + YP.escape.RED + str(variables["played"]["yz"]) + YP.escape.END + "Yahtzeeeeees!")
            print("\n")
            break
        variables["gameBegan"] = 0

        if roll == "P":
            variables = YP.GameLoop(variables)
            if variables["gameBegan"] == 0:
                variables["gameBegan"] = 1
        elif roll == "Q":
            print("\nYou make me sad! Your score Was: " + YP.escape.GREEN + str(variables["scoreDis"]) + YP.escape.END + "You got " + YP.escape.RED + str(variables["played"]["yz"]) + YP.escape.END + "Yahtzeeeeees!")
            break
        elif roll == "N":
            variables = YP.NewGame(variables)
        else:
            print("ERROR, ERROR!! But of course you knew that make a proper selection, this isn't yutzee!")
            variables["gameBegan"] = 1

main(gameVars)