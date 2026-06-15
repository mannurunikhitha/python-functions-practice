def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_strong(n):
    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10

    return total == n

num = int(input("Enter a number: "))

if is_strong(num):
    print("Strong Number")
else:
    print("Not a Strong Number")