#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    a, b = 0,1
    for i in range(0,n):
        a,b = b, a + b
    return a

print(fibonacci(60))
#>>> 14930352