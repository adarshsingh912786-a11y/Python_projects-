def password_check(user_name,password):
    user = input("Enter the user name:  ")
    pass_word = (input("Enter the password:  "))

    if user == user_name and password == pass_word:
        print("success fully enter") 

    else:
        print("user_name or password is inccorect")

user_name = "xero"
password = "xerxx789"


password_check(user_name, password)        


    