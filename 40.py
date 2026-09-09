print("Welcome lords international ATM ")
mini_amt = 100
balance = 5000
pswrd = 123456
print ("1.balance enquiry " \
"2. cash withdrawal " \
"3. end session ")
opt = int (input(' select a option : '))
pin = int(input("enter your pin : "))
if pin == pswrd :
    if opt == 1 :
        print ("balance :",balance)
    elif opt == 2 :
        cash = int ( input ("enter amount to withdraw : "))
        if cash > balance :
            print ("insufficient balance")
        else :
            print("your transaction is being processed ")
            print ("amount withdrew : ",cash)
            print("balance remaining : ", balance-cash)
    else :
        print ("your session ended")