
# Tail recursion
# - Base case
# - Operations
# - Recursive call

def tail(n):
    if n == 0:
        return
    print(n)
    tail(n-1)

# Head recursion
# - Base case
# - Recursive call
# - Operations 

def head(n):
    if n == 0:
        return
    head(n-1)
    print(n)

tail(5)
head(5)
