
from termcolor import cprint
import hashlib
import random
import sqlite3

# conn = sqlite3.connect('bank.db')
# c = conn.cursor()
# c.execute('''
#     CREATE TABLE IF NOT EXISTS customers
#     (name text, adhaar text, acc_pin text, balance real, account_no integer)
# ''')
def register(c, conn):
    name = input("Enter your name: ")
    adhaar=input("enter your adhaar no.:")
    acc_pin= input("set pin:")
    balance = float(input("Enter initial deposit: "))
    account_no = random.randint(10**15, 10**16 - 1)
    hashed_pin = hashlib.sha256(acc_pin.encode()).hexdigest()

    c.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?)",
        (name, adhaar, hashed_pin, balance, account_no))
    conn.commit()
    

    cprint(f"Account created for {name} with initial deposit of {balance}. a/c ending with {str(account_no)[-4:]}", 'green')

  