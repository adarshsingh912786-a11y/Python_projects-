import random

second_player = 0
first_player = 0
while True:
    
    score = random.randint(0 , 6)
    if score == 0:
        print(f" Total : {first_player}")
        print("you are out")
        break

    else :
        first_player += score
        print(score)
        
while True:
    
    score = random.randint(0 , 6)
    if score == 0:
        print(f" Total : {second_player}")
        print("you are out")
        break

    else :
        second_player += score
        print(score)

if first_player > second_player:
    print("The first player is win ")  

else:
    print("The second player is win")



         
        










