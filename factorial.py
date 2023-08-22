def head(n):
    if n == 0:
        return 1
    return head(n-1) * n 

def tail(n, accumulator = 1):
    if n == 0:
        return accumulator
    return tail(n - 1, accumulator * n)

print(head(10))
print(tail(10))