#Guess The Number
import random
number = random.randint (0,100)
a = True
while a == True:
    user_input = int (input ("Guess the number from 0-100: "))
    if user_input < number:
        print ("Please input a higher number")
    if user_input > number:
        print ("Please input a lower number")
       
    if user_input == number:
        a == False
        print (f"Your guess is right!, {number} is the number")
        break