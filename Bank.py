'''
Design a software for bank system. There should be options like cash withdraw,
cash credit and change password. According to user input,
the software should provide required output.
'''


balance = 25000
def CashWithdrawal():
    try:
        PIN = int(input('Enter PIN to proceed:'))
        if PIN == 1234:
            amount = int(input('Enter the amount : '))
            global balance
            balance -= amount
            print('Current balance is ', balance)
            print('Thank You For Banking With Us')
        else:
            print('You Have Entered Invalid PIN. Try Again')
    except:
        print('Invalid entry')


def CashDeposit():
    try:
        PIN = int(input('Enter ATM PIN to proceed :'))
        if PIN == 1234:
            amount = int(input('Enter Amount That You Wish to Deposit :'))
            global balance
            balance += amount
            print('Current balance is ', balance)
            print('Thank You For Banking With Us')
        else:
            print('You Have Entered Invalid PIN. Try Again')
    except:
        print('Invalid entry')

def ChangePin():
    try:
        PIN = int(input('Enter ATM or CARD PIN to proceed :'))
        if PIN == 1234:
            new_pwd1 = int(input('Please Enter Your new Password :'))
            new_pwd2 = int(input('Please Enter Your new Password again :'))
            if new_pwd1 == new_pwd2:
                PIN = new_pwd1
                print("PIN changed successfully")
                print('Thank You For Banking With Us')
        else:
            print('You Have Entered Invalid PIN. Try Again')
    except:
        print('Invalid entry')


print('Welcome to XYZ Bank\nChoose from below options')
print('1. Case withdrawal\n2. Cash credit\n3. Change password')
while True:
    opt = int(input('Enter your option:'))
    if opt == 1:
        CashWithdrawal()
        break
    elif opt == 2:
        CashDeposit()
        break
    elif opt == 3:
        ChangePin()
        break
    else:
        print('Invalid entry')
        continue