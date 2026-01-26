def add_task():
    task = input("Enter the task: ")

    with open("book.txt","w") as h:
        h.write(task + "\n")

def view():
    pass

def delete_task(task):
    pass

def main():
    print("$$$$$ To-do list $$$$$")
    print("1.Add Task \n2.View Task \n3.Detete Task")
    user = int(input("Enter the choice in number given above: "))

    if user == 1:
        add_task()

main()

