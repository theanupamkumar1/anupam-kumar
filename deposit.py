def deposit(c, conn, name):
    amount = float(input("Enter the amount to deposit: "))
    c.execute("UPDATE customers SET balance = balance + ? WHERE name = ?", (amount, name))
    conn.commit()
    print(f"You have deposited {amount}.")