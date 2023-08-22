def fibonacci_iteration(n):
    a, b = 0 ,1
    
    while n > 0:
        n = n - 1
        a, b = b, a + b
 
    return a


print(fibonacci_iteration(4))