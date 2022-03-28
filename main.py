class Account:
    
    def __init__(self):
        self.balance=0
        print('Your Account is Created.')
  
    def deposit(self):
  
        amount=int(input('Enter the amount to deposit: '))
        self.balance+=amount
        print('Your New Balance =%d ' %self.balance)

    def withdraw(self):
  
        amount=int(input('Enter the amount to withdraw:'))
        if(amount>self.balance):
            print('Insufficient Balance.')
        else:
            self.balance-=amount
            print('Your Remaining Balance =%d ' %self.balance)

    def balance(self):
        print('Your Balance =%d' %self.balance)

account = Account()
  
prompt = input("Enter 1 for balance\nEnter 2 for deposits\nEnter 3 for withdrawls\nEnter 0 to exit ")
prompt = int(prompt)

if prompt == 1:
  account.balance()
elif prompt == 2:
  account.deposit()
elif prompt == 3:
  account.withdraw()
elif prompt == 0:
    print("Come again soon.")
else:
  print("Invalid entry. Please restart.")
