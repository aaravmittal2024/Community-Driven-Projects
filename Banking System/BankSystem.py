class Account:
    def __init__(self, name, account_number, password, balance=0):
        self.name = name
        self.account_number = account_number
        self.password = password
        self.balance = balance
        self.interest_rate = 0.05  # Assuming a 5% annual interest rate
        self.loan_amount = 0
        self.loan_interest_rate = 0.10  # Assuming a 10% annual loan interest rate
        self.transactions = []  # To store account transactions
        self.next = None

    # Method to add a transaction entry
    def add_transaction(self, description):
        self.transactions.append(description)

class BankingSystem:
    # Define currency conversion rates to USD
    CURRENCY_RATES = {
        'EUR': 1.20, 'GBP': 1.40, 'JPY': 0.0091, 'USD': 1.0, 'CAD': 0.80, 
        'AUD': 0.70, 'NZD': 0.68, 'CHF': 1.05, 'ZAR': 0.07, 'CNY': 0.15,
        'INR': 0.013, 'BRL': 0.18, 'RUB': 0.014, 'KRW': 0.0009, 'MXN': 0.05,
        'SGD': 0.75, 'HKD': 0.13, 'NOK': 0.11, 'SEK': 0.12, 'DKK': 0.16,
        'TRY': 0.09, 'IDR': 0.00007, 'MYR': 0.24, 'PLN': 0.26, 'PHP': 0.02,
        'ILS': 0.30, 'THB': 0.03, 'ARS': 0.01, 'CZK': 0.045, 'CLP': 0.0013,
        'TWD': 0.035, 'AED': 0.27, 'VEF': 0.0001, 'PEN': 0.25, 'HUF': 0.0032,
        'COL': 0.0003, 'PKR': 0.006, 'EGP': 0.063, 'LBP': 0.00066, 'VND': 0.00004,
        'BDT': 0.012, 'KZT': 0.0024, 'IQD': 0.0007, 'DZD': 0.0075, 'LYD': 0.72,
        'UYU': 0.023, 'MAD': 0.11, 'XPF': 0.0097, 'CRC': 0.0016, 'BOB': 0.14
    }

    def __init__(self):
        self.head = None

    def create_account(self, name, password):
        if not self.head:
            self.head = Account(name, 0, password)
            current = self.head
        else:
            current = self.head
            prev = None
            while current:
                prev = current
                current = current.next

            current = Account(name, prev.account_number + 1, password)
            prev.next = current

        print(f"Account created successfully! Your account number is: {current.account_number}")

    def authenticate(self, account_number, password):
        current = self.head
        while current:
            if current.account_number == account_number and current.password == password:
                return current
            current = current.next
        return None

    def has_sufficient_funds(self, account, amount):
        return account.balance >= amount

    def deposit(self, account, amount):
        account.balance += amount
        account.add_transaction(f"Deposited: ${amount}")
        print(f"Deposited ${amount}. New balance: ${account.balance}")

    def withdraw(self, account, amount):
        # Removed the check for has_sufficient_funds, to allow negative balances
        account.balance -= amount
        account.add_transaction(f"Withdrew: ${amount}")
        print(f"Withdrew ${amount}. New balance: ${account.balance}")

    def transfer(self, source_account, target_account_number, amount):
        if source_account.account_number == target_account_number:
            print("You cannot transfer money to the same account!")
            return

        target_account = self.get_account_by_number(target_account_number)
        if not target_account:
            print("Target account not found!")
            return

        if not self.has_sufficient_funds(source_account, amount):
            print("Insufficient balance!")
            return

        source_account.balance -= amount
        target_account.balance += amount
        source_account.add_transaction(f"Transferred ${amount} to account {target_account_number}")
        target_account.add_transaction(f"Received ${amount} from account {source_account.account_number}")
        print(f"Transferred ${amount} to account {target_account_number}. Your new balance: ${source_account.balance}")

    def get_account_by_number(self, account_number):
        current = self.head
        while current:
            if current.account_number == account_number:
                return current
            current = current.next
        return None

    def apply_interest(self, account):
        interest = account.balance * account.interest_rate
        account.balance += interest
        account.add_transaction(f"Interest Applied: ${interest}")
        print(f"Interest of ${interest} applied. New balance: ${account.balance}")

    def apply_for_loan(self, account, amount):
        account.loan_amount += amount
        account.balance += amount
        account.add_transaction(f"Loan Taken: ${amount}")
        print(f"Loan of ${amount} taken. New balance: ${account.balance}")

    def repay_loan(self, account, amount):
        if account.balance < amount:
            print("Insufficient balance to repay the loan!")
            return
        account.loan_amount -= amount
        account.balance -= amount
        account.add_transaction(f"Loan Repaid: ${amount}")
        print(f"Repayed loan of ${amount}. Remaining loan: ${account.loan_amount}")

    def display_transactions(self, account):
        print("\nRecent Transactions:")
        for transaction in reversed(account.transactions[-5:]):  # Displaying last 5 transactions
            print(transaction)

    def currency_conversion(self, currency, amount):
        if currency in BankingSystem.CURRENCY_RATES:
            return amount * BankingSystem.CURRENCY_RATES[currency]
        else:
            print("Currency not supported!")
            return 0

bank = BankingSystem()

while True:
    print("\nBanking System:")
    print("1. Create account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        password = input("Set your password: ")
        bank.create_account(name, password)

    elif choice == "2":
        account_number = int(input("Enter your account number: "))
        password = input("Enter your password: ")
        account = bank.authenticate(account_number, password)

        if account:
            while True:
                print("\nWelcome, {}!".format(account.name))
                print("1. Check balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. Apply Interest")
                print("6. Take Loan")
                print("7. Repay Loan")
                print("8. View Transactions")
                print("9. Currency Exchange")
                print("10. Logout")
                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    print("Your balance is: ${}".format(account.balance))
                elif user_choice == "2":
                    amount = float(input("Enter the amount to deposit: "))
                    bank.deposit(account, amount)
                elif user_choice == "3":
                    amount = float(input("Enter the amount to withdraw: "))
                    bank.withdraw(account, amount)
                elif user_choice == "4":
                    target_account_number = int(input("Enter the target account number: "))
                    amount = float(input("Enter the amount to transfer: "))
                    bank.transfer(account, target_account_number, amount)
                elif user_choice == "5":
                    bank.apply_interest(account)
                elif user_choice == "6":
                    amount = float(input("Enter the loan amount: "))
                    bank.apply_for_loan(account, amount)
                elif user_choice == "7":
                    amount = float(input("Enter the loan repayment amount: "))
                    bank.repay_loan(account, amount)
                elif user_choice == "8":
                    bank.display_transactions(account)
                elif user_choice == "9":
                    print("Supported currencies for conversion to USD:", ', '.join(BankingSystem.CURRENCY_RATES.keys()))
                    currency = input("Enter the currency code you want to convert from: ").upper()
                    amount_in_foreign_currency = float(input(f"Enter the amount in {currency}: "))
                    
                    # Convert currency to USD
                    amount_in_usd = bank.currency_conversion(currency, amount_in_foreign_currency)
                    
                    if amount_in_usd > 0:
                        print(f"{amount_in_foreign_currency} {currency} is equal to ${amount_in_usd} USD.")
                        action = input("Do you want to (1) Deposit or (2) Withdraw this amount in USD? ")
                        
                        if action == "1":
                            bank.deposit(account, amount_in_usd)
                        elif action == "2":
                            bank.withdraw(account, amount_in_usd)
                    else:
                        print("Unable to perform the conversion.")
                elif user_choice == "10":
                    break

        else:
            print("Authentication failed!")

    elif choice == "3":
        print("Thank you for using the banking system!")
        break
