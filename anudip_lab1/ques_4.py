a=int(input("enter first side: "))
b=int(input("enter second side: "))
c=int(input("enter second side: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(f"The area of the triangle is {area}")