import random
import string

lenght = int(input("Enter the lenght of your password you want: ").strip())

user_upper = input("you wnat upper in password (y/n):  ").lower() == "y"
user_lower = input("you want lower in password (y/n):  ").lower() == "y"
user_digit = input("you want digit in password (y/n):  ").lower() == "y"
user_special =input("you want special in password (y/n):  ").lower() == "y"


upper = string.ascii_uppercase
lower = string.ascii_lowercase
digit = string.digits
special = string.punctuation

char = ""

if user_upper:
    char+= upper

if user_lower:
    char+= lower

if user_digit:
    char+= digit

if user_special:
    char+= special

if not char:
    print("Error: no charcter type has been selected")

password = ""

for _ in range(lenght):
    password += random.choice(char)

print(f"this is your best password: {password}") 

print("Thank you")






    

    






