class Bank:
    def __init__(self, correct_pin, balance = 0):
        self.correct_pin = correct_pin
        self.balance = balance

    def pin_verify(self, entered_pin):
        if entered_pin == self.correct_pin:
            return True 
        else: 
            return False
        
    def display_balance(self, entered_pin):
        if self.pin_verify(entered_pin):
            print(f"Your Account Balance Is : {self.balance}")

    def withdraw(self, entered_pin, amount):
        if self.pin_verify(entered_pin):
            if amount >= self.balance: 
                print("Insufficient Funds")
            else: 
                self.balance -= amount
                print(f"Withdrawl Amount : {amount}")
                print(f"Remaining Balance : {self.balance}")
    
    def deposit(self, entered_pin, amount):
        if self.pin_verify(entered_pin):
            self.balance += amount
            print(f"Deposit Amount : {amount}")
            print(f"Updated Balance : {self.balance}")

my_acc = Bank(correct_pin=1234, balance=500) 

my_acc.display_balance(1234)    # Output : Your Account Balance Is : 500
my_acc.withdraw(1234, 100)      # Output : Withdrawl Amount : 100, Remaining Balance : 400
my_acc.deposit(1234, 200)       # Output : Deposit Amount : 200, Updated Balance : 600
my_acc.withdraw(1234, 700)      # Output : Insufficient Funds