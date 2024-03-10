

def inquiry(c, conn, name):
    c.execute("SELECT balance FROM customers WHERE name = ?", (name,))
    result = c.fetchone()

    if result is not None:
        balance = result[0]
        print(f"Your current balance is {balance}.")
    else:
        print("No account found with that name.")