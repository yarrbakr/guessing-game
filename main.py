# minimum viable product (MVP)

# 1. random number generator
import random

# 3. points scoring system:
points : int = 0

# checking function:
def check_num( points):
        random_number : int = random.randint(1,10)
        user_input : int = int(input("Enter your choice: "))
        if user_input == random_number:
                print("Congratulations")
                points += 1
                print(f"points: {points}") 
        else:
                print("Better luck next time")
                points -= 1
                print(f"points: {points}")

check_num( points)
choice : str = input("Play again(Y/N): ")
if choice.upper() == "Y" :
        check_num( points)
else:
    print("Goodbye!!")
    