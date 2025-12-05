class Atm:
    def __init__(self):
        self.pin = None
        self.balance = 0
    def create_pin(self):
        self.pin = input("Create your new PIN: ")
        self.balance = float(input("Enter initial balance: "))
        print("PIN created successfully!")
        self.menu()
    def change_pin(self):
        old_pin = input("Enter your current PIN: ")
        if old_pin != self.pin:
            print("Enter correct pin!")
        else:
            new_pin = input("Enter new PIN: ")
            self.pin = new_pin
            print("PIN changed successfully!")
        self.menu()
    def check_balance(self):
        entered_pin = input("Enter your PIN to check balance: ")
        if entered_pin != self.pin:
            print("Enter correct pin!")
        else:
            print("Your current balance is:", self.balance)
        self.menu()
    def withdraw(self):
        entered_pin = input("Enter your PIN: ")

        if entered_pin != self.pin:
            print("Enter correct pin!")
        else:
            amount = float(input("Enter amount to withdraw: "))
            if amount > self.balance:
                print("Insufficient funds!")
            else:
                self.balance -= amount
                print("Withdraw successful! New balance:", self.balance)
        self.menu()
    def deposit(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin != self.pin:
            print("Enter correct pin!")
        else:
            amount = float(input("Enter amount to deposit: "))
            self.balance += amount
            print("Deposit successful! New balance:", self.balance)
        self.menu()
    def menu(self):
        print("\n----- ATM Menu -----")
        print("1. Create PIN")
        print("2. Change PIN")
        print("3. Check Balance")
        print("4. Withdraw Money")
        print("5. Deposit Money")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.create_pin()
        elif choice == '2':
            self.change_pin()
        elif choice == '3':
            self.check_balance()
        elif choice == '4':
            self.withdraw()
        elif choice == '5':
            self.deposit()
        elif choice == '6':
            print("Thanks for using ATM. Goodbye!")
        else:
            print("Invalid choice!")
            self.menu()
atm = Atm()
atm.menu()