def head(n):
    if n <= 2:
        return 1
    return head(n - 1) + head(n - 2)

def tail(n, accumulator1 = 0, accumulator2 = 1):
    if n == 0:
        return accumulator1
    if n == 1:
        return accumulator2
    sum = accumulator1 + accumulator2
    return tail(n-1,accumulator2, sum)

print(tail(10))
print(head(10))