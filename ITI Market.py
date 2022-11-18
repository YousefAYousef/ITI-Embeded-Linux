shopping = [{"id": 1, "Name": "Bannana", "Price": 25},
            {"id": 2, "Name": "Pinaple", "Price": 20},
            {"id": 3, "Name": "Guava","Price": 18},
            {"id": 4, "Name": "APPLE", "Price": 27}]

shopping1 = shopping
temp = []
order = ""


def adminLoginWindow():
    print("=====================")
    print("1.Display Menu")
    print("2.Add Product")
    print("3.Remove Product")
    print("4.Logout")
    print("=====================")


def adminDisplayMenuWindow():
    print("Id\tName\tAvailable\tPrice\tOriginal Price")
    print("====================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t\t{d["Price"]}')


def addproducts():
    n = int(input("Enter the no.of.items need to be added : "))
    for i in range(n):
        new_id = int(input("Enter id : "))
        new_Name = input("Enter Name : ")
        new_Price = int(input("Enter Price : "))
        d = [{"id": new_id, "Name": new_Name, "Price": new_Price}]
        shopping.extend(d)
        adminDisplayMenuWindow()


def removeproducts():
    dressId = int(input("Enter the id need to be deleted : "))
    found = False
    for d in shopping1:
        found = d["id"] == dressId
        if found != True:
            temp.append(d)
            continue
    print("Deleting item....")
    if len(temp) == d:
        print(f"{dressId} not found")
    else:
        print(f"{dressId}'s one available is removed from the list")
    adminDisplayMenuWindow()

def logoutwindow():
    login()


def adminOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 2:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        addproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 3:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        removeproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 4:
        logoutwindow()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()


def userLoginWindow():
    print("=====================\n")
    print("1.Display Menu")
    print("2.Place order")
    print("4.Logout")
    print("\n======================")


def userDisplayMenuWindow():
    print("Id\tName\tAvailable\tPrice")
    print("===================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Price"]}')

def user_id():
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))

def placeOrder():
    order_number = 10
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))

    for d in shopping:
        if d["id"] == p_id:
            print("\nId\tName\tAvailable\tPrice")
            print("=============================================================")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Price"]}')
            order = '{d["id"]}\t{d["Name"]}\t{d["Price"]}'
            conform = input("\nDo you want to place an order on the above shown product : Y/N ")

            if conform == 'Y' or conform == 'y':
                print("\nSuccessfully placed the order on the product {} {}".format(d["id"], d["Name"]))
                order_number += 1
                print("Your order number is : ", order_number)
                break

            elif conform == 'N' or conform == 'n':
                print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                break

    if d["id"] != p_id:
        print("\nYou have entered invalid id. Please enter valid id\n")
        user_id()
    print("\nAvailable products : \n")
    userDisplayMenuWindow()

def userChoiceOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        userDisplayMenuWindow()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 2:
        placeOrder()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 3:
        logoutwindow()
    else:
        print("Invalid Choice. Please enter valid choice")

def login():
    tp = input("Login Admin/Login User [Type A to Login in the Admin/ Type U to Login in the User] : ")
    if tp == 'A' or tp == 'a':
        password = input("Enter the password : ")
        if password == "a123":
            adminLoginWindow()
            adminOptions()
        else:
            print("Invalid password. Please enter valid password")

    elif tp == 'U' or tp == 'u':
        password = input("Enter the password : ")
        if (password == "u123"):
            userLoginWindow()
            userChoiceOptions()
        else:
            print("Invalid password. Please enter valid password")
    else:
        print("Invalid user type. Enter valid user type")


login()









