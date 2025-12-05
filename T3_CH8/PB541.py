class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def Deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("Amount deposited:", amount)
        print("Updated balance:", self.balance)
    def Withdrawal(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Updated balance:", self.balance)
    def display(self):
        print("\n----- Account Details -----")
        print("Account Number:", self.accountNumber)
        print("Account Holder Name:", self.name)
        print("Balance:", self.balance)
        print("---------------------------")
acc_no = int(input("Enter Account Number: "))
name = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))
acc = BankAccount(acc_no, name, balance)
while True:
    print("\n----- Menu -----")
    print("1. Display Account Details")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        acc.display()
    elif choice == '2':
        acc.Deposit()
    elif choice == '3':
        acc.Withdrawal()
    elif choice == '4':
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")