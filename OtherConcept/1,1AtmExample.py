class Atm :  
    def __init__(self):
        self.pin = "" 
        self.balance = 0  
        self.menu()
    
    def menu(self) :  
        user_input  = input (""" 
        Hii How can I help You ? 
        1. Press 1 to create pin 
        2. Press 2 to change pin 
        3. Press 3 to check balance 
        4. Press 4 to withdraw Money 
        5. Press Anythink to Exit 
        """)
        if user_input == "1" : 
            # create pin func 
            self.create_pin() 
        elif user_input == "2" : 
            # Change pin  
            self.change_pin()
        elif user_input == "3" : 
            # Check Balance 
            self.check_balance()
        elif user_input == "4" : 
            # Money Withdraw
            self.withdraw_money()  

    def create_pin(self) : 
        user_pin = input("Enter Your Pin ") 
        self.pin = user_pin
        user_balance = input("Enter Your Balance") 
        self.balance = user_balance
        print("PIN CREATED Successfully")
        self.menu()

    def change_pin(self):
        old_pin= input("Enter your old pin = ") 
        if old_pin == self.pin: 
            new_pin = input("Enter New Pin = ") 
            if new_pin == old_pin: 
                print("New Pin cannot same as Old pin Enter new ") 
            else:
                self.pin = new_pin  
                print("Pin changed Successfully") 
            
        else: 
            print("Entered Incorrect Pin") 
        self.menu() 
    def check_balance(self): 
        print("Your Balance is ",self.balance) 
        self.menu() 
    # These functions are called Methods 
    def withdraw_money(self) :  
        user_pin = input("Enter Pin = ")   
        if user_pin != self.pin: 
            print("Enter Correct Pin") 
          
        else:
            with_money = input("Enter Money for withdraw = ")
            if with_money > self.balance:
                print("You don't have ", with_money, " to withdraw.Your current balance is ", self.balance)  
               
            else: 
                self.balance = self.balance- int(with_money)
                print("WithDraw Successfully. Your Current Balance is ",self.balance) 
        self.menu()
    
# If function is inside a class call method or if they outside of class then they called function 
# like len()  -> function   and a.append()  is method 
p = Atm()  