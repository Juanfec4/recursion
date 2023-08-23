def gcd_recursion(a,b):
    rem = a % b
    if rem == 0: 
        return b
    return gcd_recursion(b, rem)

def gcd_iteration(a,b):
    rem = a % b
    while rem != 0:
        rem = a % b
        a, b = b, rem
    return b

print(gcd_iteration(64,16))