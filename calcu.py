a = int(input("Enter the first value:  "))
b = int(input("Enter the second value:  "))

print(" 1.add"
      " 2.sub"
      " 3.mul"
      " 4.divide")

user = input("Please select the option given above: ")

  

add = a+b
sub = a-b
mul = a*b
divide = a/b

if(user ==  "add") :
    print(f"your answer is:  {add}")

if(user ==  "sub"):
    print(f"your answer is:  {sub}")    

if(user ==  "mul"):
    print(f"your answer is:   {mul}")

if(user ==  "divide"):
    print(f"your answer is:   {divide}")

else:
    print("Enter the right option and please enter the word not number ")