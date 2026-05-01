# Rock Paper Scissors Lizard Spock
# https://www.codedex.io/@COOLmanYT/build/rock-paper-scissors-lizard-spock
# Made for Project Checkpoint in Codedex for Python course (but I am too broke to actually do it)

import random

def main():
    print("""================================
Rock Paper Scissors Lizard Spock
================================
    
1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖""")

    try:
        player = int(input("Pick a number: "))
    except ValueError:
        print("Please enter a number!")
        return
    if player < 1 or player > 5: # answer validation
        print("Invalid choice!")
        return
    
    computer = random.randint(1, 5)

    def num_to_emoji(num):
        if num == 1:
            return '✊'
        elif num == 2:
            return '✋'
        elif num == 3:
            return '✌️'
        elif num == 4:
            return '🦎'
        else:
            return '🖖'

    def win_calc(p1, p2):
        if p1 == p2:
            return "It was a tie!"
        if (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2):
            return "You won!" # standard RPS rules
        if (p1 == 4 and p2 == 5) or (p1 == 5 and p2 == 3) or (p1 == 3 and p2 == 4) or (p1 == 4 and p2 == 2) or (p1 == 2 and p2 == 5) or (p1 == 5 and p2 == 1):
            return "You won!" # additional Lizard Spock rules
        else:
            return "You lost!"

    print("")
    print("You chose: " + num_to_emoji(player))
    print("Computer chose: " + num_to_emoji(computer))
    print(win_calc(player, computer))

    play_again = input("Play again? (y/n) ")
    if play_again == "y":
        main()
    else:
        print("Thanks for playing!")
        exit()

if __name__ == "__main__":
    main()