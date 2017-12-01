import random

def start():
    invalid = True
    while invalid:
        print("Would you like to start the card game? (y/n)")
        ans = input("> ")
        if ans[0].lower() == "y":
            return ans
            invalid = False
        elif ans[0].lower() == "n":
            return ans
            invalid = False
        else:
            print("Sorry, that's not a valid answer.")

def end():
    invalid = True
    while invalid:
            print("Would you like to quit the card game? (y/n)")
            ans = input("> ")
            if ans[0].lower() == "y":
                return ans
                invalid = False
            elif ans[0].lower() == "n":
                return ans
                invalid = False
            else:
                print("Sorry, that's not a valid answer.")

def game():
    cards = []
    coins = 500
    running = True
    while running:
        print("Type HELP if you would like a list of commands and how to play.\nIf you already know how to play, go ahead and type a command.")
        ans = input("> ")
        if ans.lower() == "help":
            print("""

                    Welcome to the card game.
                    There are 4 levels of cards:
                    4*, 3*, 2*, and 1* (in order of most to least rarity)
                    It costs 50 coins to draw 10 cards.
                    To get more coins, sell your existing cards.
                    The higher the rarity of the card, the more coins you can get for it.
                    4* cards give you 100 coins. 3* cards give you 50 coins.
                    2* cards give you 25 coins. 1* cards give you 5 coins.
                    Here is the chance to pull each card rarity:
                    4* = 1%
                    3* = 4%
                    2* = 15%
                    1* = 80%

                    Here is a list of commands:
                    DECK - view deck/card inventory
                    DRAW - draw ten cards
                    SELL - sell cards
                    COIN - view coin amount
                    QUIT- quit the game

                    We give you 500 coins to start! Have fun!
                    
                  """)
        elif ans.lower() == "quit":
            break
        
        else:
            print("Sorry that's not a valid answer. Please try again.")
game_loop = True
while game_loop:
    begin = start()

    if begin[0].lower() == "y":
        game()
        break
    else:
        endq = end()

    if endq[0].lower() == "y":
        quit()
    else:
        pass

print("You've reached the end of the file.")
    
