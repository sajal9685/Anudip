quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
total = quantity * price
if total > 5000:
    total *= 0.9
print("Total expense:", total)
