def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev

num = int(input("Enter a number: "))
print("Reverse Number =", reverse_number(num))