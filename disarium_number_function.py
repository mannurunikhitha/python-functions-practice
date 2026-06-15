def is_disarium(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        digits -= 1
        temp //= 10

    return total == n

num = int(input("Enter a number: "))

if is_disarium(num):
    print("Disarium Number")
else:
    print("Not a Disarium Number")