# 'Guess Who?' Game V2
import time
import random

def ask_yes_no(question):
    while True:
        answer = input(question + " (Y/N): ").lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        elif answer == "exit":
            exit()
        elif answer == "debug information":
            print(characters)
            print(actionsDone)
            print("Version 2.1 of the Guess Who? Game by someone COOL")
            print("Public version")
        else:
            print("Please answer with 'Y' or 'N'.")

characters = [
    "Amy", "David", "Leo", "Gabe", "Katie", "Olivia", "Jordan", "Carmen",
    "Laura", "Joe", "Mike", "Al", "Daniel", "Sophia", "Nick", "Lily",
    "Liz", "Mia", "Emma", "Rachel", "Ben", "Eric", "Farah", "Sam"
]

actionsDone = []

# Welcome message
print("Welcome to the Guess Who? Game!")
print("This program will try to guess the character you're thinking of in 6 questions or less.")
print("Please pick a character from the 24 available choices.")
print(characters)

time.sleep(3)

def remove(char_list, names):
    if isinstance(names, str):
        # Single name
        if names in char_list:
            char_list.remove(names)
    else:
        # List of names
        for name in names:
            if name in char_list:
                char_list.remove(name)

# Game starts here
malequestion = ask_yes_no("Is your character male?")
if malequestion == True:
    print("Your character is male.")
    remove(characters, ["Amy", "Katie", "Olivia", "Carmen", "Sophia", "Lily", "Mia", "Emma", "Liz", "Rachel", "Farah", "Laura"])
    actionsDone.append("Is your character male? (Responded TRUE)")
    print("Remaining characters: " + str(characters))
    time.sleep(3)
    malechoice = True
if malequestion == False:
    print("Your character is female.")
    remove(characters, ["David", "Leo", "Gabe", "Jordan", "Mike", "Daniel", "Nick", "Eric", "Sam", "Ben", "Joe", "Al"])
    actionsDone.append("Is your character male? (Responded FALSE)")
    print("Remaining characters: " + str(characters))
    time.sleep(3)
    malechoice = False

glassesquestion = ask_yes_no("Does your character wear glasses?")
if glassesquestion == True:
    remove(characters, ["David", "Leo", "Gabe", "Jordan", "Laura", "Mike", "Eric", "Sam", "Daniel", "Katie", "Nick", "Olivia", "Carmen", "Sophia", "Lily", "Mia", "Emma", "Farah" ]) # fix this!
    actionsDone.append("Does your character wear glasses? (Responded TRUE)")
    print("Remaining characters: " + str(characters))
    time.sleep(3)
    glasseschoice = True
if glassesquestion == False:
    remove(characters, ["Amy", "Joe", "Daniel", "Nick", "Liz", "Farah"])
    actionsDone.append("Does your character wear glasses? (Responded TRUE)")
    print("Remaining characters: " + str(characters))
    time.sleep(3)
    glasseschoice = False

# very hard desicion split process
if malechoice == True and glasseschoice == True: # path 1
    path1question1 = ask_yes_no("Does your character wear RED glasses? ")
    if path1question1 == True:
        remove(characters, ["Al", "Joe"])
        print("Your character is BEN!")
        actionsDone.append("Does your character wear RED glasses? (Responded TRUE)")
        print("Actions completed:" + str(actionsDone))
        print("Thanks for playing!") 
        time.sleep(5)
        exit()
    if path1question1 == False:
        remove(characters, "Ben")
        print("Remaining characters: " + str(characters))
        actionsDone.append("Does your character wear RED glasses? (Responded FALSE)")
        path1question2 = ask_yes_no("Does your character have a beard?")
        if path1question2 == True:
            remove(characters, "Joe")
            print("Your character is AL!")
            actionsDone.append("Does your character have a beard? (Responded TRUE)")
            print("Actions completed:" + str(actionsDone))
            print("Thanks for playing!") 
            time.sleep(5)
            exit()
        if path1question2 == False:
            remove(characters, "Al")
            print("Your character is JOE!")
            actionsDone.append("Does your character have a beard? (Responded FALSE)")
            print("Actions completed:" + str(actionsDone))
            print("Thanks for playing!") 
            time.sleep(5)
            exit()

if malechoice == False and glasseschoice == True: # path 2
    path2question1 = ask_yes_no("Does your character have white hair? ")
    if path2question1 == True:
        remove(characters, ["Rachel", "Amy"])
        print("Your character is LIZ!")
        actionsDone.append("Does your character have white hair? (Responded TRUE)")
        print("Actions completed:" + str(actionsDone))
        print("Thanks for playing!") 
        time.sleep(5)
        exit()
    if path2question1 == False:
        remove(characters, "Liz")
        print("Remaining characters: " + str(characters))
        actionsDone.append("Does your character have white hair? (Responded FALSE)")
        path2question2 = ask_yes_no("Does your character have white glasses? ")
        if path2question2 == True:
            remove(characters, "Amy")
            print("Your character is RACHEL!")
            actionsDone.append("Does your character have white glasses? (Responded TRUE)")
            print("Actions completed:" + str(actionsDone))
            print("Thanks for playing!") 
            time.sleep(5)
            exit()
        if path2question2 == False:
            remove(characters, "Rachel")
            print("Your character is AMY!")
            actionsDone.append("Does your character have white glasses? (Responded FALSE)")
            print("Actions completed:" + str(actionsDone))
            print("Thanks for playing!") 
            time.sleep(5)
            exit()

if malechoice == True and glasseschoice == False: # path 3
    path3question1 = ask_yes_no("Does your character have ANY black hair? ")
    if path3question1 == True:
        remove(characters, ["David", "Leo", "Daniel", "Nick"])
        print("Remaining characters: " + str(characters))
        actionsDone.append("Does your character have ANY black hair? (Responded TRUE)")
        path3question2 = ask_yes_no("Does your character have anything on their head? (Other than hair) ")
        if path3question2 == True:  
            remove(characters, ["Gabe", "Eric", "Jordan"])
            print("Remaining characters: " + str(characters))
            actionsDone.append("Does your character have anything on their head? (Responded TRUE)")
            path3question3 = ask_yes_no("Does your character like the trumpet? ")
        if path3question2 == False:
            remove(characters, ["Sam", "Mike"])
            print("Remaining characters: " + str(characters))
            actionsDone.append("Does your character have anything on their head? (Responded FALSE)")
            path3question3_2 = ask_yes_no("Does your character like the guitar? ")
            if path3question3_2 == True:
                remove(characters, ["Jordan", "Gabe"])
                print("Your character is ERIC!")
                actionsDone.append("Does your character like the guitar? (Responded TRUE)")
                print("Actions completed:" + str(actionsDone))
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
            if path3question3_2 == False:
                remove(characters, "Eric")
                print("Remaining characters: " + str(characters))
                actionsDone.append("Does your character like the guitar? (Responded FALSE)")
                path3question4 = ask_yes_no("Does your character have dyed hair? ")
                if path3question4 == True:
                    remove(characters, "Gabe")
                    print("Your character is JORDAN!")
                    actionsDone.append("Does your character have dyed hair? (Responded TRUE)")
                    print("Actions completed:" + str(actionsDone))
                    print("Thanks for playing!") 
                    time.sleep(5)
                    exit()
                if path3question4 == False:
                    remove(characters, "Jordan")
                    print("Your character is GABE!")
                    actionsDone.append("Does your character have dyed hair? (Responded FALSE)")
                    print("Actions completed:" + str(actionsDone))
                    print("Thanks for playing!") 
                    time.sleep(5)
                    exit()
            if path3question3 == True:
                remove(characters, "Mike")
                print("Your character is SAM!")
                actionsDone.append("Does your character like the trumpet? (Responded TRUE)")
                print("Actions completed:" + str(actionsDone))
                print("Thanks for playing!")
                time.sleep(5)
                exit()
            if path3question3 == False:
                remove(characters, "Sam")
                print("Your character is MIKE!")
                actionsDone.append("Does your character like the trumpet? (Responded FALSE)")
                print("Actions completed:" + str(actionsDone))
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
    if path3question1 == False:
        remove(characters, ["Gabe", "Jordan", "Eric", "Sam", "Mike"])
        print("Remaining characters: " + str(characters))
        actionsDone.append("Does your character have ANY black hair? (Responded FALSE)")
        path3question2 = ask_yes_no("Does your character have blonde hair? ")
        if path3question2 == True:
            remove(characters, ["Daniel", "Leo"])
            print("Remaining characters: " + str(characters))
            actionsDone.append("Does your character have blonde hair? (Responded TRUE)")
            path3question3 = ask_yes_no("Does your character have a blue cap? ")
        if path3question2 == False:
            remove(characters, ["David", "Nick"])
            print("Remaining characters: " + str(characters))
            actionsDone.append("Does your character have blonde hair? (Responded FALSE)")
            path3question3_1 = ask_yes_no("Does your character have white hair? ")
            if path3question3_1 == True:
                remove(characters, "Daniel")
                print("Your character is LEO!")
                actionsDone.append("Does your character have white hair? (Responded TRUE)")
                print("Actions completed:" + str(actionsDone))
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
            if path3question3_1 == False:
                remove(characters, "Leo")
                print("Your character is DANIEL!")
                actionsDone.append("Does your character have white hair? (Responded FALSE)")
                print("Actions completed:" + str(actionsDone))
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
            if path3question3 == True:
                remove(characters, "Nick")
                print("Your character is DAVID!")
                actionsDone.append("Does your character have a blue cap? (Responded TRUE)")
                print("Actions completed:" + str(actionsDone))
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
            if path3question3 == False:
                remove(characters, "David")
                print("Your character is NICK!")
                actionsDone.append("Does your character have a blue cap? (Responded FALSE)")
                print("Actions completed:" + str(actionsDone))
                print("Thanks for playing!") 
                time.sleep(5)
                exit()

if malechoice == False and glasseschoice == False: # path 4
    path4question1 = ask_yes_no("Does your character have ANY black hair?")
    if path4question1 == True:
        remove(characters, ["Katie", "Lily", "Sophia", "Carmen", "Emma"])
        actionsDone.append("Does your character have ANY black hair? (Responded TRUE)")
        print("Remaining characters:" + str(characters))
        time.sleep(3)
        path4question2 = ask_yes_no("Does your character like animals?")
        if path4question2 == True:
            remove(characters, ["Olivia", "Laura"])
            actionsDone.append("Does your character like animals? (Responded TRUE)")
            print("Remaining characters:" + str(characters))
            time.sleep(3)
            path4question3 = ask_yes_no("Does your character like fish?")
            if path4question3 == True:
                remove(characters, ["Mia"])
                print("Your character is FARAH!")
                actionsDone.append("Does your character like fish? (Responded TRUE)")
                print("Actions completed:" + str(actionsDone))
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
            if path4question3 == False:
                remove(characters, "Farah")
                print("Your character is MIA!")
                actionsDone.append("Does your character likr fish? (Responded FALSE)")
                print("Actions completed:" + str(actionsDone))
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
        if path4question2 == False:
            remove(characters, ["Farah", "Mia"])
            actionsDone.append("Does your character like animals? (Responded FALSE)")
            print("Remaining characters:" + str(characters))
            time.sleep(3)
            path4question3 = ask_yes_no("Does your character have both red and black hair?")
            if path4question3 == True:
                remove(characters, "Laura")
                print("Your character is OLIVIA!")
                actionsDone.append("Does your character have white hair? (Responded TRUE)")
                print("Actions completed" + str(actionsDone))
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
            if path4question3 == False:
                remove(characters, "Olivia")
                print("Your character is LAURA!")
                actionsDone.append("Does your character have white hair? (Responded TRUE)")
                print("Actions completed" + str(actionsDone))
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
    if path4question1 == False:
        remove(characters, ["Farah", "Mia", "Laura", "Olivia"])
        actionsDone.append("Does your character have ANY black hair? (Responded FALSE)")
        print("Remaining characters:" + str(characters))
        time.sleep(3)
        path4question2 = ask_yes_no("Does your character have a hat (or anything excluding hair on their head)? ")
        if path4question2 == True:
            remove(characters, ["Sophia", "Carmen", "Emma"])
            actionsDone.append("Does your character have a hat (or anything excluding hair on their head)? (Responded TRUE)")
            print("Remaining characters:" + str(characters))
            time.sleep(3)
            path4question3 = ask_yes_no("Do they have blond hair?")
            if path4question3 == True:
                remove(characters, "Lily")
                print("Your character is KATIE!")
                actionsDone.append("Does your character have blond hair? (Responded TRUE)")
                print("Actions completed" + actionsDone)
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
            if path4question3 == False:
                remove(characters, "Katie")
                print("Your character is LIZ!")
                actionsDone.append("Does your character have blond hair? (Responded FALSE)")
                print("Actions completed" + actionsDone)
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
        if path4question3 ==  False:
            remove(characters, ["Katie", "Lily"])
            actionsDone.append("Does your character have a hat (or anything excluding hair on their head)? (Responded FALSE)")
            print("Remaining characters:" + str(characters))
            time.sleep(3)
            path4question4 = ask_yes_no("Does your character have red hair?")
            if path4question4 == True:
                remove(characters, ["Sophia", "Carmen"])
                print("Your character is EMMA!")
                actionsDone.append("Does your character have red hair? (Responded TRUE)")
                print("Actions completed" + actionsDone)
                print("Thanks for playing!") 
                time.sleep(5)
                exit()
            if path4question4 == False:
                remove(characters, "Emma")
                actionsDone.append("Does your character have red hair? (Responded FALSE)")
                print("Remaining characters:" + str(characters))
                time.sleep(3)
                path4question5 = ask_yes_no("Does your character have white hair?")
                if path4question5 == True:
                    remove(characters, "Sophia")
                    print("Your character is CARMEN!")
                    actionsDone.append("Does your character have white hair? (Responded TRUE)")
                    print("Actions completed" + actionsDone)
                    print("Thanks for playing!") 
                    time.sleep(5)
                    exit()
                if path4question5 == False:
                    remove(characters, "Carmen")
                    print("Your character is LIZ!")
                    actionsDone.append("Does your character have white hair? (Responded FALSE)")
                    print("Actions completed" + actionsDone)
                    print("Thanks for playing!") 
                    time.sleep(5)
                    exit()

print("If you are still here...")
print("Something probably went wrong. :| ")
print(characters)
print(actionsDone)
exit()

# end of game
# made by someone COOL
# Thanks for playing!