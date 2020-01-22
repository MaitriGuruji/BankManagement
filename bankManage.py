import pymongo

def addCust():

    Name=input("Enter Name : ")
    while True:
        Usrname=input("Enter User Name: ")
        t = mycol.find_one({"UsrName": Usrname})
        if t==None:
            break
        else:
            print("Username Already exists! try again.")

    DOB = input("Enter DOB : ")
    Phn = input("Enter Phone Number : ")
    mydict = {"Name": Name,"UsrName":Usrname, "DOB": DOB, "Phn No": Phn, "Balance": 0}
    x = mycol.insert_one(mydict)

def delCust():
    print("Enter Usrname of custemer you want to delete record of : ")
    n=input()
    myquery = {"UsrName": n}
    mycol.delete_one(myquery)

def editCust():
    un=input("Enter Username of the customer: ")
    c=input("What do you want to edit ? Name/DOB/Phn no : ")
    v=input("Enter the new value")
    mycol.update_one({'UsrName': un},{'$set':{c: v}})

def dispCust():
    for x in mycol.find():
        print(x)

def amountWD():

    un=input("Enter Your usrname: ")
    t=mycol.find_one({"UsrName":un})
    b=t['Balance']
    print("Your Balance is {}".format(b))
    print("Do you want to withdraw or deposit? : ")
    c=input()
    if c in "withdraw":
        amount=int(input("Enter Amount : "))
        if amount<=b:
            newB=b-amount
            mycol.update_one({'UsrName': un}, {'$set': {"Balance":newB}})
            print("Transaction successfull.")
            t = mycol.find_one({"UsrName": un})
            b = t['Balance']
            print("Your current balance is {}".format(b))
        else:
            print("Not enough balance.")

    elif c in "deposit":
        amount = int(input("Enter Amount : "))
        if amount<=0:
            print("Enter valid amount.")
        else:
            newB = b + amount
            mycol.update_one({'UsrName': un}, {'$set': {"Balance":newB}})
            print("Transaction successfull.")
            t = mycol.find_one({"UsrName": un})
            b = t['Balance']
            print("Your current balance is {}".format(b))

    else:
        print("Wrong choice.")


def options(argument):
    switcher = {
        1:addCust,
        2:delCust,
        3:editCust,
        4:dispCust,
        5:amountWD,
        6:exit,
    }
    funct = switcher.get(argument, lambda: "Invalid Choice")
    funct()

if __name__ == "__main__":

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["BankDB"]
    mycol = mydb["Customers"]

    while True:

        print("\nSelect any option from below: ")
        print("****************************************************************")
        print("1. Add Customer")
        print("2. Delete Customer")
        print("3. Edit Customer Details")
        print("4. Display all Customer Details")
        print("5. Withdraw and Deposit Amount")
        print("6. Exit")
        print("***************************************************************")

        options(int(input("Enter your choice : ")))


