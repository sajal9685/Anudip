distance = float(input("Enter distance to travel (in km): "))

if distance <= 50:
    fare = distance * 8
elif distance <= 100:
    fare = distance * 10
else:
    fare = distance * 12

print(f"Total fare: Rs. {fare:.2f}")
