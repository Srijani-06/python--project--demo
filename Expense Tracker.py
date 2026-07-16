import datetime


def add_expense():
    amount = float(input("Enter the amount"))
    category = input("Enter the category")
    notes = input("Enter notes")
    date = str (datetime.date.today())

    f = open("Expenses.txt" , "a")
    f.write(str(amount) + "," + category + ","+ notes + "," + date + "\n")
    f.close()

def view_expense():
    view = input("What you want to view:")
    f = open ("Expenses.txt" , "r")
    found = False

    for line in f :
        expense = line.strip().split(",")
        

        if expense[1].lower() == view.lower():
            print("amount" , expense[0])
            print("category" , expense[1])
            print("notes" , expense[2])
            print("date" , expense[3])
            found = True
            break

    if not found:
        print("Expense not found")

    f.close()

def delete_expense():
    delete = input("What you want to delete:")
    f = open ("Expenses.txt" , "r")
    lines = f.readlines()
    f.close()

    f = open("Expenses.txt" ,"w")
    found = False

    for line in f:
        expense = line.strip().split(",")
    

        if expense[1].lower() == delete.lower():
            found = True
            print("DELETED")

        else:
            f.write(line)

    if not found:
        print("EXPENSE NOT FOUND")

    f.close()



def calclulate_expense():
    total = 0 

    calculate = input ("what type of calculation do you want:calculate by(category/date):")
    
    if calculate == "category":
        category = input("Enter Category:")
    elif calculate == "date":
        date = input("Enter date")

    f = open ("Expenses.txt" , "r")
    found = False

    for line in f :
        expense = line.strip().split(",")

        if calculate == "category":
           if expense[1].lower() == category.lower():
              add_amount = float(expense[0])
              total = total + add_amount
              found = True 

        elif calculate == "date":
           if expense[3].lower() == date.lower():
              add_amount = float(expense[0])
              total = total + add_amount
              found = True 

    if found :
      print("showing the total:")
      print(total)
    else:
        print("No expense found:")


while True:
    print("\n1.add_expense")
    print("2.view_expense")
    print("3.delete_expense")
    print("4.calculate_expense")
    print("exit")

    choice = input("WHAT YOU WANT TO CHOOSE IN EXPENSE:")

    if choice == "1":
        add_expense()
        print("Added to Expense")
    elif choice == "2":
        view_expense()
        print("Expense viewed")
    elif choice == "3":
        delete_expense()
        print("Expense deleted")
    elif choice == "4" :
        calclulate_expense()
        print(" expense calculated")
    elif choice == "5" :
        print("goodbye")


    