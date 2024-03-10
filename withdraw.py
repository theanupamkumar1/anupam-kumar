def withdraw(c, conn, name):
    amount = float(input("Enter the amount to withdraw: "))
    c.execute("SELECT balance FROM customers WHERE name = ?", (name,))
    result = c.fetchone()

    if result is not None:
        balance = result[0]
        if amount <= balance:
            c.execute("UPDATE customers SET balance = balance - ? WHERE name = ?", (amount, name))
            conn.commit()
            print(f"You have withdrawn {amount}. Your new balance is {balance - amount}.")
        else:
            print("Insufficient balance.")
    else:
        print("No account found with that name.")