print("Toy Codes: 1 = Battery Based, 2 = Key-based, 3 = Electrical Charging")
code = int(input("Enter toy code (1/2/3): "))
amount = float(input("Enter order amount: "))

if code == 1:
    if amount > 1000:
        discount = 0.10 * amount
    else:
        discount = 0
elif code == 2:
    if amount > 100:
        discount = 0.05 * amount
    else:
        discount = 0
elif code == 3:
    if amount > 500:
        discount = 0.10 * amount
    else:
        discount = 0
else:
    print("Invalid toy code.")
    discount = 0

net_amount = amount - discount
print(f"Discount: Rs. {discount:.2f}")
print(f"Net amount to pay: Rs. {net_amount:.2f}")
