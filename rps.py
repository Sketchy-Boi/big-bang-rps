import random

# Yeah that IS alot of if's and elif's
#You'll have to re-run the function to play again, too lazy to code otherwise.
#Feedback would be nice (SketchyBoi#9799)


#main function, no args or parameters
def rockpaperscissorslizardspock():
    print("Welcome to Rock Paper Scissors Lizard Spock. You will be playing against a computer, this is totally not rigged")
    print("This is a variation of the standard rock paper scissors from the Big Bang Theory")
    user_play = str(input("Type your choice. (rock / paper / scissors / lizard / spock) "))
    possible_plays = ["rock", "paper", "scissors", "lizard", "spock"]
    cpu_play = random.choice(possible_plays)
    print(f"You chose {user_play}, computer chose {cpu_play}!")
    if user_play.lower() == cpu_play.lower():
        print("Tie!")
    elif user_play.lower() == "rock":
        if cpu_play.lower() == "scissors":
            print("Rock smashes scissors. You Win!")
        elif cpu_play.lower() == "lizard":
            print("Rock squishes lizard. You Win!")
        elif cpu_play.lower() == "paper":
            print("Paper covers rock. CPU Wins!")
        elif cpu_play.lower() == "spock":
            print("Spock melts rock. CPU Wins!")    
    elif user_play.lower() == "paper":
        if cpu_play.lower() == "rock":
            print("Paper covers rock. You Win!")
        elif cpu_play.lower() == "spock":
            print("Paper disproves spock. You Win!")
        elif cpu_play.lower() == "lizard":
            print("Lizard eats paper. CPU Wins!")
        elif cpu_play.lower() == "scissors":
            print("Scissors cut paper. CPU Wins!")
    elif user_play.lower() == "scissors":
        if cpu_play.lower() == "paper":
            print("Scissors cut paper. You Win!")
        elif cpu_play.lower() == "rock":
            print("Rock smashes scissors. CPU Wins!")
        elif cpu_play.lower() == "lizard":
            print("Scissors decapitate lizard. You Win!")
        elif cpu_play.lower() == "spock":
            print("Spock destroys scissors. CPU Wins!")
    elif user_play.lower() == "lizard":
        if cpu_play.lower() == "rock":
            print("Rock squishes lizard. CPU Wins!")
        elif cpu_play.lower() == "paper":
            print("Lizard eats paper. You Win!")
        elif cpu_play.lower() == "scissors":
            print("Scissors decapitate lizard. CPU Wins!")
        elif cpu_play.lower() == "spock":
            print("Lizard poisons spock. You Win")
    elif user_play.lower() == "spock":
        if cpu_play.lower() == "rock":
            print("Spock melts rock. You Win!")
        elif cpu_play.lower() == "scissors":
            print("Spock destroys scissors. You Win!")
        elif cpu_play.lower() == "paper":
            print("Paper disproves spock. CPU Wins!")
        elif cpu_play.lower() == "lizard":
            print("Lizard poisons spock. CPU Wins!")
    else:
        print("Unknown Input. Are you sure you entered one of the choices in the list?")



    


