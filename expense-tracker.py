#--------------EXPENSE TRACKER PROJECT----------------

import json
expenses=[] 
print("welcome to expense tracker: SPEND WISELY")
while True:
    print("========MENU=======")
    print("1. ADD EXPENSE")
    print("2. VIEW ALL EXPENSE")
    print("3. VIEW TOTAL EXPENSE")
    print("4. SAVE TO JSON")
    print("5. EXIT")

    choice=input("please enter your choice?")

    #1. ADD EXPENSE
    if choice=="1":
        date=input("date: DD-MM-YY ")
        category=input("where do you spend?")
        description=input("any extra details of category?")
        amount=float(input("enter the amount:"))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenses.append(expense)
        print("\ndone dude, expense added successfully.")

    #2. VIEW ALL EXPENSE
    elif choice == "2":
        if len(expenses) == 0:
            print("no expenses recorded yet")
        else:
            print("\n ----All Expenses-----")
            i=1
            for e in expenses:
                print(f"{i} -->{e['date']} |{e['category']} |{e['description']} | {e['amount']}")
                i+=1
            print("------------------------------------")

    #3. VIEW TOTAL EXPENSE
    elif choice == "3":
        total=0
        for e in expenses :
            total+=e["amount"]
        print(f"\n total spending = {total}")

    #4.SAVE TO JSON
    elif choice =="4":
        if len(expenses)==0:
            print("no expenses to save")
        else:
            try:
                with open("expenses.json","w") as file:
                    json.dump(expenses,file,indent=4)
                print("\nexpenses saved successfully to expenses.json")
            except Exception as e:
                print("error saving file:",e)


    #5. EXIT
    elif choice == "5":
        print("\n thanks for using expense tracker!" )
        break

    # for invalid choice
    else:
        print("invalid choice. please try again")

