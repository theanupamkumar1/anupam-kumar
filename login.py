from inquiry import inquiry
from withdraw import withdraw
from deposit import deposit
from change_pin import change_pin
from termcolor import cprint

import hashlib

def login(c, conn):
    name = input("Enter your name: ")
    entered_pin = input("Enter your pin: ")
    hashed_entered_pin = hashlib.sha256(entered_pin.encode()).hexdigest()

    c.execute("SELECT acc_pin FROM customers WHERE name = ?", (name,))
    result = c.fetchone()

    if result is not None:
        stored_pin = result[0]
        if hashed_entered_pin == stored_pin:
            cprint(f"Welcome back, {name}!", "green")
        else:
            print("Incorrect PIN.")
            return False

        while True:
            print("1: Inquiry")
            print("2: Withdraw")
            print("3: Deposit")
            print("4: Change PIN")
            print("5: Logout")
            action = input("Enter your action: ")

            if action == '1':
                inquiry(c, conn, name)
            elif action == '2':
                withdraw(c, conn, name)
            elif action == '3':
                deposit(c, conn, name)
            elif action == '4':
                change_pin(c, conn, name)
            elif action == '5':
                break
            else:
                print("Invalid action. Please enter a valid action.") 

    else:
        cprint("No account found with that name.", "red")