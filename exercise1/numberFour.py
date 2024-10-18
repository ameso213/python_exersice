class WITIAcademySacco:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 1000:
            print("Minimum deposit amount is 1000.")
        else:
            self.balance += amount
            print(f"Successfully deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount < 500:
            print("Minimum withdrawal amount is 500.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew {amount}. New balance is {self.balance}.")

    def check_balance(self):
        print(f"Your current balance is {self.balance}.")

def main():
    sacco = WITIAcademySacco()
    
    while True:
        print("\nWelcome to WITI Academy Sacco.")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            sacco.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            sacco.withdraw(amount)
        elif choice == '3':
            sacco.check_balance()
        elif choice == '4':
            print("Thank you for using WITI Academy Sacco!")
            break
        else:
            print("Invalid option. Please select again.")

if __name__ == "__main__":
    main()
