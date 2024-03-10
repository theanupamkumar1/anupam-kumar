# from bank import Bank
# from customer import Customer
# from account import Account
import sqlite3



# conn = sqlite3.connect('bank.db')
# c = conn.cursor()
# c.execute('''
#     CREATE TABLE IF NOT EXISTS customers
#     (name text, adhaar text, acc_pin text, initial_deposit real, account_no integer)
# ''')
# def main():
#     bank = Bank()

#     while True:
#         print("\nWelcome to the Bank!")
#         print("1. Create an account")
#         print("2. Login")
#         print("3. forget pin")
#         print("4. Quit")

#         choice = input("Choose an option: ")

#         if choice == '1':
#             name = input("Enter your name: ")
#             adhaar=input("enter your adhaar no.:")
#             acc_pin= input("set pin:")
#             initial_deposit = float(input("Enter initial deposit: "))
#             account_no = random.randint(10**15, 10**16 - 1)
#             hashed_pin = hashlib.sha256(acc_pin.encode()).hexdigest()

#             c.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?)",
#               (name, adhaar, hashed_pin, initial_deposit, account_no))

            
#             print(f"Account created for {name} with initial deposit of {initial_deposit}. a/c ending with {account_no[12:]} ")

#         elif choice == '2':
#             name = input("Enter your name: ")
#             entered_pin = input("Enter your pin: ")
#             hashed_entered_pin = hashlib.sha256(entered_pin.encode()).hexdigest()

#             c.execute("SELECT acc_pin FROM customers WHERE name = ?", (name,))
#             result = c.fetchone()

#             if result is not None:
#                 stored_pin = result[0]
#                 if hashed_entered_pin == stored_pin:
#                     print(f"Welcome back, {name}!")
#                     # Here you can add more options for the user like deposit, withdraw, check balance etc.
#                 else:
#                     print("Incorrect PIN.")
#             else:
#                 print("No account found with that name.")

#         elif choice == '3':
#             name = input("Enter your name: ")
#             adhaar = input("Enter your Aadhaar no.: ")

#             c.execute("SELECT adhaar FROM customers WHERE name = ?", (name,))
#             result = c.fetchone()

#             if result is not None:
#                 stored_adhaar = result[0]
#                 if adhaar == stored_adhaar:
#                     new_pin = input("Enter new pin: ")
#                     hashed_new_pin = hashlib.sha256(new_pin.encode()).hexdigest()
#                     c.execute("UPDATE customers SET acc_pin = ? WHERE name = ?", (hashed_new_pin, name))
#                     conn.commit()
#                     print(f"PIN for {name} has been reset.")
#                 else:
#                     print("Incorrect Aadhaar number.")
#             else:
#                 print("No account found with that name.")

#         elif choice == '4':
#             print("You have chosen to quit. Thank you for banking with us!")
#             break

#         else:
#             print("Invalid option. Please choose a valid option.")

# if __name__ == "__main__":
#     main()

#--------------------------------------------------

from login import login
from register import register
from forget import forget
import os

def main():
    # Connect to the database and create a cursor
    if not os.path.exists('bank.db'):
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS customers
        (name text, adhaar text, acc_pin text, balance real, account_no integer)
    ''')
        conn.commit()
    else:
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
    

    while True:
        
        print("\nWelcome to the Bank!")
        print("1. Create an account")
        print("2. Login")
        print("3. forget pin")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register(c, conn)
        elif choice == '2':
            login(c, conn)
        elif choice == '3':
            forget(c, conn)
        elif choice == '4':
            print("You have chosen to quit. Thank you for banking with us!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()