ram = int(input("Enter age of Ram: "))
sulabh = int(input("Enter age of Sulabh: "))
ajay = int(input("Enter age of Ajay: "))
youngest = min(ram, sulabh, ajay)
if youngest == ram:
    print("Ram is the youngest")
elif youngest == sulabh:
    print("Sulabh is the youngest")
else:
    print("Ajay is the youngest")
