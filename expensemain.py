from dataofexpense import (
    create_table,
    add_expense,
    view_expense,
    delete_expense

)

def main():

    create_table()

    while True:
        print("\n-------- Expense Tracker -------")
        print("1. Add Expenses \n2. View Expense Record \n3. Delete Expense \n4.Exit")

        choice = int(input("Choose from menu (1-4):  "))

        if choice == 1:

            amount = float(input("Enter the amount of expense : ")) 
            category = input("Enter Expense category: ")
            date = input("Enter the date of expense (YYYY-MM-DD): ")
            note = input("Enter the reason of expense: ")
            add_expense(amount, category, date, note)
            print("Record Saved successfully")

        elif choice == 2:

            expenses = view_expense()
            print("\n $$$$$$ All Expenses $$$$$$\n")

            for ex in expenses:
                print(f"{ex[0]}.{ex[1]}|{ex[2]}|{ex[3]}|{ex[4]}")

        elif choice == 3:

            expenses = view_expense()
            print("\n $$$$$$ All Expense $$$$$$\n")

            for ex in expenses:
                print(f"{ex[0]}.{ex[1]}|{ex[2]}|{ex[3]}|{ex[4]}")

            expense_id = int(input("\n Enter the expense id to delete: "))

            delete_expense(expense_id)
            print("\n One Expense Delete Successfully")        


        elif choice ==  4:
            print("Done with updation!")
            break
        else:
            print("Enter the choice in range!")

if __name__ == "__main__":
    main()
