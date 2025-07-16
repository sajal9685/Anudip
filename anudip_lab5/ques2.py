rows = 5
for i in range(1, rows + 1):
    print("  " * (rows - i), end="")
    val = i
    for j in range(1, i):
        print(val, end=" ")
        val += 1
    for j in range(i):
        print(val, end=" ")
        val -= 1
    print()
