class Account:
    def __init__(self,account_number:str,account_holder:str,balance:int) -> None:
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f'Successfull deposit of {amount}. Your balance is now {self.balance}')
    def withdraw(self,amount):
        if amount>self.balance:
            print('Desired amount exceeds balance. Please try lower amount')
        else:
            self.balance-=amount
            print(f'You have withdrawn {amount}! Your current balance is {self.balance}')
    def __str__(self) -> str:
        return f"Name: {self.account_holder}\nAcc.number: {self.account_number}\nBalance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, account_number: str, account_holder: str, balance: int,interest_rate:int) -> None:
        super().__init__(account_number, account_holder, balance)
        self.interest_rate=interest_rate
    def apply_interest(self):
        get_interest=self.interest_rate*self.balance
        self.balance+=get_interest
        print(f'You get your interest of {get_interest} to your account! your balance now is {self.balance}')
class CurrentAccount(Account):
    def __init__(self, account_number: str, account_holder: str, balance: int,overdraft_limit:int) -> None:
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit=overdraft_limit
    def withdraw(self, amount):
        if self.balance+self.overdraft_limit>=amount:
            self.balance-=amount
            print(f'You have been able to withdraw {amount}. Your balance now is {self.balance}')
        else:
            print('Not enough funds. Try with lower amount')

class Bank:
    def __init__(self,bank_name:str) -> None:
        self.bank_name=bank_name
        self.accounts_storage=[]
    def find_account_by_account_number(self,account_number):
        for i in self.accounts_storage:
            
            if i.account_number==account_number:
                return i
        return None
            
    def add_account(self,account):
        search_result=self.find_account_by_account_number(account.account_number)
        if not search_result:

            self.accounts_storage.append(account)
            print(f'{account.account_holder} has been added to the bank')
        else:
            print('There is already existing account')
    def deposit(self,account_number,amount):
        search_result=self.find_account_by_account_number(account_number) 
        if search_result:
            return search_result.deposit(amount)
        else:
            return 'Account doesnt exist'
            
    def withdraw(self,account_number,amount):
        search_result=self.find_account_by_account_number(account_number)
        if search_result:
           return search_result.withdraw(amount)
        else:
            return 'Account doesnt exist'
    def list_accounts(self):
        if not self.accounts_storage:
            print('\nNo accounts in the bank')
        else:
            print('Our bank accounts')
            for account in self.accounts_storage:
                print(f'\nAccount holder: {account.account_holder} \nAccount number: {account.account_number} \nBalance: {account.balance} ')
            print(f'There are {len(self.accounts_storage)} accounts in the bank')
            

if __name__=="__main__":
    my_bank=Bank("UBS")
    my_bank.add_account(SavingsAccount("1001", "Alice", 5000, 0.03))
    my_bank.add_account(CurrentAccount("1002", "Bob", 3000, 1000))
    my_bank.add_account(SavingsAccount("1003", "Charlie", 7000, 0.04))

    while True:
        print("\nBank Menu")
        print("1. List all accounts")
        print("2. Add account")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Apply interest (Savings Account)")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice=='1':
            my_bank.list_accounts()
        elif choice=='2':
            account_type=""
            while not account_type:
                account_type=input('Please input Saving(S)/Current(C) account')
            while account_type!='C' and account_type!='S':
                    account_type=input(' Saving(S)/Current(C) ')
                    print(account_type)
            account_number=input('Please input Account number')
            account_holder=input('Please input Account name')
            account_balance=int(input('How much money would you like to deposit?'))

            if account_type=='C':
                overdraft_limit=float(input('Please insert overdraft limit: '))
                my_bank.add_account(CurrentAccount(account_number,account_holder,account_balance,overdraft_limit))
                print('Account added')
               
            elif account_type=='S':
                interest_rate=float(input('Please insert your interest rate'))
                my_bank.add_account(SavingsAccount(account_number,account_holder,account_balance,interest_rate))
                print('Account added')
                
            # print('Account added')
        elif choice=='3':
            account_number=input('account number: ')
            deposit_amount=float(input('How much money would you like to deposit?'))
            
            print(my_bank.deposit(account_number,deposit_amount))
        elif choice=='4':
            account_number=input('account number: ')
            withdraw_amount=float(input('How much money would you like to deposit?'))
            
            print(my_bank.withdraw(account_number,withdraw_amount))
        elif choice=='5':
            account_number=input('account number: ')
            account=my_bank.find_account_by_account_number(account_number)
            if isinstance(account,SavingsAccount):
                print(account.apply_interest())
            else:
                print('This is not a saving account')


        elif choice=='6':
            break