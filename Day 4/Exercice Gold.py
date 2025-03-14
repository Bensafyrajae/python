class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
        else:
            raise Exception("Authentication failed!")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated!")
        if amount <= 0:
            raise Exception("Deposit amount must be positive!")
        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated!")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive!")
        if amount > self.balance:
            raise Exception("Insufficient funds!")
        self.balance -= amount

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated!")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive!")
        if self.balance - amount < self.minimum_balance:
            raise Exception("Cannot withdraw below minimum balance!")
        self.balance -= amount

class ATM:
    def __init__(self, account_list, try_limit=2):
        if not isinstance(account_list, list) or not all(isinstance(acc, BankAccount) for acc in account_list):
            raise Exception("Invalid account list!")
        if not isinstance(try_limit, int) or try_limit <= 0:
            try_limit = 2
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("1. Log in")
            print("2. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid option!")

    def log_in(self, username, password):
        for account in self.account_list:
            try:
                account.authenticate(username, password)
                print("Login successful!")
                self.show_account_menu(account)
                return
            except:
                continue
        self.current_tries += 1
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down.")
            exit()
        else:
            print("Invalid credentials. Try again.")

    def show_account_menu(self, account):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                amount = int(input("Enter deposit amount: "))
                try:
                    account.deposit(amount)
                    print("Deposit successful! New balance:", account.balance)
                except Exception as e:
                    print(e)
            elif choice == "2":
                amount = int(input("Enter withdrawal amount: "))
                try:
                    account.withdraw(amount)
                    print("Withdrawal successful! New balance:", account.balance)
                except Exception as e:
                    print(e)
            elif choice == "3":
                print("Logging out.")
                break
            else:
                print("Invalid option!")
