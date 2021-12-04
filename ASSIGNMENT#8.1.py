#Lottery
import random
ticket = []
lottery = []
a = True
while a == True:
    #Get the user's lucky numbers
    for i in range (3):
        user_ticket = int (input ("Put your lucky number: "))
        ticket.append (user_ticket)
    print ("This is your ticket ", ticket)
    #Generate random numbers
    for i in range (3):
        winning_number = random.randint (0,9)
        lottery.append (winning_number)
    print ("The winning numbers are ", lottery)
    #Match numbers in ticket and in lottery
    if ticket in lottery:
        print ("You Win, Congratulations")
    else:
        print ("You Lose, Please try again")
    #Ask the player to play again
    another_ticket = input ("Do you want to try again? (type 'y' if yes, and 'n' if no): ")
    another_ticket.lower
    if another_ticket == 'y':
        continue 
    if another_ticket == 'n':
        a == False
        break
    else:
        a == False
        break
