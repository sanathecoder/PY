import math 
import random
user = input("Guess the Number: ")


num = random.randint(1,10)
if(user == num):
    print("You Won The number was", num)
    
else:
    print("Try Again . The number was", num)
print("Thanks for playing")