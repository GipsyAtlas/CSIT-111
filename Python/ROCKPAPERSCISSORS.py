# My name is Oluwatimilehin Amoo from CSIT 111 CLW
# I edited this program to ask the player if they want to play rock or paper or scissors instead of 1 or 2 or 3.
# I also included an input validation loop

# Edit explanations
    # first I changed the inputanswer from 1,2,3 to rock paper scissors.
    # second I changed the players inputanswer choice in the def whowon from the num(1,2,3) to word(rock,paper,scissors).
    # third I changed any word that was playerNum to playerword.
    # forth I included an input validation loop for if the play doesn't enter rock or paper or scissors and enters somthing else.
    
#RockPaperScissors
#logic from Starting Out with Programming Logic and Design by Tony Gaddis
#Written in Python and modified by Veronica Noone for academic purposes

#include random mod so we can have the computer make a choice
import random

#The getNumber module gets the users choice
def getword():
    inputAnswer = input ("\nEnter rock or paper or scissors: ")
    while inputAnswer not in ('rock', 'paper', 'scissors'):
        print("Invalid input Please enter rock or paper or scissors.")
        inputAnswer = input ("\nEnter rock or paper or scissors: ")
    return inputAnswer
#End Module

#The showWinner module display who wins -- calls whoWon function
def showWinner(computer, player):
    print('\nComputer chose', whichChoice(computer))
    print('Player chose', (player), '\n')
    if computer == player:
        print("Player made same choice. Play again.")
    else:
        which = whoWon(computer, player)
        if which == 1:
            print("Computer wins.")
        else:
            if which == 2:
                print("Player wins.")
            else:
                print("No winner.")
            #end If
        #end If
    #end If
#End Module
                
#The whichChoice function displays choice
def whichChoice(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    else:
        return "scissors"
    #end If
#End Function
 
#The whoWon function selects winner
def whoWon(computer, player):
# 1 = rock, 2 = paper, 3 = scissors
# rock smashes scissors
# scissors cuts paper
# paper wraps rock
# both choose same no winner
    if computer == player:
        return 0
    #end If
    
# test computer chose rock
    if computer == 1:
        if player == 'paper':
            return 2 #paper wraps rock
        elif player == 'scissors':
            return 1 #rock smashes scissors
        #end If
    #end If
        
# test computer chose paper
    if computer == 2:
        if player == 'rock':
            return 1 #paper wraps rock
        elif player == 'scissors':
            return 2 #scissors cuts paper
        #end If
    #end If
# test computer chose scissors
    if computer == 3:
        if player == 'rock':
            return 2 #rock smashes scissors
        elif player == 'paper':
            return 1 #scissors cuts paper
        #end If
    #end If
        
    return 0
#End Function



# main module
def main():
    # Get computer number
    computer = random.randint(1, 3)
    #print(computer) #uncomment for debugging
    # Get player number
    playerword = getword()
    # Show winner
    showWinner(computer, playerword)
#End Module

print("-------------------------------------------")
print("Welcome to Rock-Paper-Scissors with Python!")
print("-------------------------------------------")

again="y"
while again=="y":
    main()
    again=input('\nplay again? y or n ')
#end while

print("\n-------------------------------------------")
x=input("Thanks for playing! Click enter to exit")
