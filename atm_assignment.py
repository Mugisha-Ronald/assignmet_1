


# def myAccount():
#     accountBalance = 20000
#     pin = '123'
#     name = input('Please Enter your name: ')
#     your_PIN = int(input("Please provide your PIN number here: "))
#     if str(your_PIN) == pin:
#         amount = int(input("Please Enter amount to withdraw: "))
#         if amount < accountBalance:
#             newAmount = accountBalance - amount
#             print("You have withdrawn " + str(amount) + " and your account balance is " + str(newAmount))
#             print("Thank you for using oue services!")

#         else:
#             print("You have insufficient funds!!!")
#             amount = int(input("Please Enter correct amount: "))
#             newAmount = accountBalance - amount
#             print("You have withdrawn " + str(amount) + " and your account balance is " + str(newAmount))
#             print("Thank you for using our services!")
            
#     else:
#         print("Incorrect PIN!")
#         your_PIN = int(input("Please provide the correct PIN number here: "))
#         amount = int(input("Please Enter amount to withdraw: "))
#         if amount < accountBalance:
#             newAmount = accountBalance - amount
#             print("You have withdrawn " + str(amount) + " and your account balance is " + str(newAmount))
#             print("Thank you for using our services!")

#         else:
#             print("You have insufficient funds!!!")
#             amount = int(input("Please Enter correct amount: "))
#             newAmount = accountBalance - amount
#             print("You have withdrawn " + str(amount) + " and your account balance is " + str(newAmount))
#             print("Thank you for using our services!")

# myAccount()

# the above can be simplified to this

actualbalance = 200000
def myAccount():
    name = input("Please enter your name:")
    pin = input("Please enter your pin:")
    if pin != "2244":
        print("Your pin is invalid")
        pin = input("Please enter the correct pin:")
    amount = input("Enter amount to withdraw:")
    if int(amount) > actualbalance:
        print("You have insuffitient funds")
        amount = input("Enter valid amount to withdraw:")
    balance = actualbalance - int(amount)
    print ("You have withdrawned:" ,int(amount))
    print ("Your current balance is:" , balance)
myAccount()

