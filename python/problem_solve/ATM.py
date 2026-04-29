import time

# Multiple users data
users = {
    "akash": {"pin": 1234, "balance": 10000, "history": []},
    "rahul": {"pin": 5678, "balance": 5000, "history": []}
}

username = input("Enter username: ")

if username in users:
    attempts = 0

    while attempts < 3:
        entered_pin = int(input("Enter PIN: "))

        if entered_pin == users[username]["pin"]:
            print("Login Successful ✅")

            while True:
                print("\n--- ATM Menu ---")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Change PIN")
                print("5. Transaction History")
                print("6. Exit")

                choice = int(input("Enter choice: "))

                if choice == 1:
                    print("Balance:", users[username]["balance"])

                elif choice == 2:
                    amount = int(input("Enter amount to deposit: "))
                    users[username]["balance"] += amount
                    users[username]["history"].append(f"Deposited {amount}")
                    print("Deposit Successful")

                elif choice == 3:
                    amount = int(input("Enter amount to withdraw: "))
                    if amount <= users[username]["balance"]:
                        users[username]["balance"] -= amount
                        users[username]["history"].append(f"Withdrew {amount}")
                        print("Collect your cash")
                    else:
                        print("Insufficient Balance")

                elif choice == 4:
                    new_pin = int(input("Enter new PIN: "))
                    users[username]["pin"] = new_pin
                    print("PIN changed successfully")

                elif choice == 5:
                    print("Transaction History:")
                    for t in users[username]["history"]:
                        print("-", t)

                elif choice == 6:
                    print("Thank you for using ATM")
                    break

                else:
                    print("Invalid choice")

            break

        else:
            attempts += 1
            print("Incorrect PIN ❌")

            if attempts == 3:
                print("Too many wrong attempts! Account blocked for 2 minutes ⛔")
                time.sleep(120)  # 2 minutes wait
                print("Try again later")

else:
    print("User not found ❌")