# Rock Paper Scissors
# Made for Project Checkpoint in Codedex for Python course (but I am too broke to actually do it)

import random

def main():
    print("""===================
Rock Paper Scissors
===================

1) ✊
2) ✋
3) ✌️""")
    try:
        player = int(input("Pick a number: "))
    except ValueError:
        print("Please enter a number.")
        return
    if player < 1 or player > 3: # answer validation
        print("Invalid choice!")
        return
    
    computer = random.randint(1, 3)

    def num_to_emoji(num):
        if num == 1:
            return '✊'
        elif num == 2:
            return '✋'
        else:
            return '✌️'

    def win_calc(p1, p2):
        if p1 == p2:
            # if they are the same, it's a tie
            return "It was a tie!"
        elif (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2):
            # rock and scissors, paper and rock or scissors and paper = win
            return "You won!"
        else:
            # anything else = lose
            return "You lost!"

    print("")
    print("You chose: " + num_to_emoji(player))
    print("Computer chose: " + num_to_emoji(computer))
    print(win_calc(player, computer))
    print("==================")

    play_again = input("Play again? (y/n) ")
    if play_again == "y":
        main()
    else:
        print("Thanks for playing!")
        exit()

if __name__ == "__main__":
    main()

