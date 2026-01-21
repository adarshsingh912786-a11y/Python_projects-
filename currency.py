def currency_converter():



    print("1.dolar to rupees \n2.rupees to dolar ")


    user = input("select the currecy option: ")


    if user == "1":
        currency = float(input("Enter the curency in dolar:  "))
        output = currency*82.3
        print(f"This is your amount:  {output} rupees ")

    elif user == "2":
        currency = float(input("Enter the currency in rupees:  "))  
        output = currency/82.3
        print(f"This is your amount:  {output} dolar ")  
    
    else:
        print("please enter the right choice ")  

currency_converter()          


