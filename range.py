import random
com = random.randint(1 , 10)
def choceright():
    count = 0
    while(True):
        user = int(input("enter the number: "))
        if(user>com):
            print("go smaller please")
            count +=1
        elif(user<com):
            print("go higher please")
            count +=1  
        elif(user == com):
            print("you gase right number") 
            count +=1  
            break
    print(f"The right choice is: {user} and the no of turn is: {count}")
    if(count <= 2):
        print("you are pro")
    elif(count >=5):
        print("you are midlevel")    
    elif(count >=8):
        print("you are a noob but try again")    
        
choceright()