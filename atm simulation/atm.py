import os,time
class Atm:
    def __init__(self):
        self.details = {2546284:{"pin":3219,"balance":10000,"name":"Shubham Yadav"},
                        2546168:{"pin":3235,"balance":10000,"name":"Md Anas"}}
        self.clear()
        self.main_menu()

    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def main_menu(self):
        user_choice = int(input("""
HELLO!!! How May I Assist You?
[1] Check Balance
[2] Change Pin
[3] Withraw amount
[4] Deposit amount
                
Enter your choice :
"""))
        if user_choice == 1:
            self.CheckBalance()
        elif user_choice == 2:
            self.change_pin()
        elif user_choice == 3:
            self.withdraw()
        elif user_choice == 4:
            self.deposit()
        else:
            print("Invalid choice ")


    def authenticate(self):
            user_input = int(input("Enter account number :"))
            if user_input in self.details:
                user_pin = int(input("Enter your pin"))
                if user_pin == self.details[user_input]["pin"]:
                    return user_input
                else:
                    print("wrong pin")
                    exit()
            else:
                print("Account number not found in database")   
                exit() 


    def CheckBalance(self):
        user_input = self.authenticate()
        print(self.details[user_input]["balance"])
        time.sleep(10)
        self.main_menu()

    def change_pin(self):
        user_input = self.authenticate()
        new_pin = int(input("Enter your new pin :"))
        self.details[user_input]["pin"] = new_pin
        print("Pin updated sucessfully ")
        time.sleep(10)
        self.main_menu()

    def withdraw(self):
        user_input = self.authenticate()
        withdraw_amount = int(input("Enter amount :"))
        if withdraw_amount <= self.details[user_input]["balance"]:
            self.details[user_input]["balance"] = self.details[user_input]["balance"] - withdraw_amount
            print(f"Withdrawal sucessfully.. remaining balance is {self.details[user_input]["balance"]}")
        else:
            print("You do not have sufficient balance in your account")
        time.sleep(10)
        self.main_menu()

    def deposit(self):
        user_input = self.authenticate()
        deposit_amount = int(input("Enter deposit amount :"))
        if deposit_amount <= 1_00_000:
            self.details[user_input]["balance"] = self.details[user_input]["balance"] + deposit_amount
            print(f"Amount credited sucessfully.. Your updated balance is {self.details[user_input]["balance"]}")
        else:
            print("Sorry your account have transction limit")
        time.sleep(10)        
        self.main_menu()
        
obj = Atm()