salary = float(input("Enter basic salary: "))
if salary < 1500:
    hra = 0.1 * salary
    da = 0.9 * salary
else:
    hra = 500
    da = 0.98 * salary
gross = salary + hra + da
print("Gross salary:", gross)
