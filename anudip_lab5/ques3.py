def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

rows = 5
for i in range(rows):
    print("  " * (rows - i - 1), end="")
    for j in range(i + 1):
        val = factorial(i) // (factorial(j) * factorial(i - j))
        print(f"{val:2}", end="   ")
    print()
