def body_weight():
    
    user1 = (float(input("enter your height in cm:")))/100
    user2 = float(input("enter your weight in kg:"))
    
    formula = user2/(user1*user1)

    print(f"this is your out put: {formula} ")

    if formula < 18.5:
        print("now your under weight")

    if formula > 18.5 and formula < 24.9:
        print("now you are normal weight")

    if formula > 25 and formula < 29.9:
        print("now you are over weight")

    if formula > 30 and formula < 34.9:
        print("now you are obec class 1")

    if formula > 35 and formula < 39.9:
        print("now you are obec class 2")
    
    if formula > 40:
        print("now you are over catergary")

body_weight()     