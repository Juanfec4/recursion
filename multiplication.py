def multiply(a,b):
    if a == 0:
        return 0
    if a < 0:
        return multiply (a + 1, b) - b;
    return multiply(a - 1, b) + b

print(multiply(-3,-4))