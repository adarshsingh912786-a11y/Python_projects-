def palin_drom():

    print("$$$$$$$ The Palindrom #######")

    user = input("Enter the string:  ").lower().strip()
    palindrom = user[::-1]

    if user == palindrom:
        print(" Yes this a plaindrome ")

    else:
        print(" Not a palindrome ") 

palin_drom()    


