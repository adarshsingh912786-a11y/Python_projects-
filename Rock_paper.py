import random
def rockpaper():
    print("r for Rock\np for paper\ns for scissor")
    co = random.choice(["r","p", "s"])

    user = input("enter the choise: ")
    print(f"Computer is choose : {co}")

    if(co == "r" and user == "p"):
        print("you  win")

    elif(co == "r" and user == "s"):
        print("computer  win")

    elif(co == "p" and user == "r"):
        print("computer is win") 

    elif(co == "s" and user == "r"):
        print("you win")

    elif(co == "s" and user == "p"):
        print("computer is win")

    elif(co == "p"  and user == "s"):
        print("you win")
    elif(co==user):
        print("It`s a draw!")
rockpaper()



        
    
    
        

    
    
        




     
    