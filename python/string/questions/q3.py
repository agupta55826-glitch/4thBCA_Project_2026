amount=int(input("enter total amount: "))
if amount >=5000:
    print("eligibal for discount")
    print("Enter mode of payment:")
    mode=input(" A-cash B-card C-UPI:")
if mode=="B":
    print("Discount Applied")
elif mode=="A" or mode=="C":
    print("Discount not applied")
else:
    print("Invalid input")
                   