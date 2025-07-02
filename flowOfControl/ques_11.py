ch = input("Enter a character: ")
ascii_val = ord(ch)
if 65 <= ascii_val <= 90:
    print("Capital letter")
elif 97 <= ascii_val <= 122:
    print("Small case letter")
elif 48 <= ascii_val <= 57:
    print("Digit")
else:
    print("Special symbol")
