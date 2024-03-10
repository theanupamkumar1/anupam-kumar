import hashlib

def forget(c, conn):
    name = input("Enter your name: ")
    adhaar = input("Enter your Aadhaar no.: ")

    c.execute("SELECT adhaar FROM customers WHERE name = ?", (name,))
    result = c.fetchone()

    if result is not None:
        stored_adhaar = result[0]
        if adhaar == stored_adhaar:
            new_pin = input("Enter new pin: ")
            hashed_new_pin = hashlib.sha256(new_pin.encode()).hexdigest()
            c.execute("UPDATE customers SET acc_pin = ? WHERE name = ?", (hashed_new_pin, name))
            conn.commit()
            print(f"PIN for {name} has been reset.")
        else:
            print("Incorrect Aadhaar number.")
    else:
        print("No account found with that name.")