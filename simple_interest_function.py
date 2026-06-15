def simple_interest(p, t, r):
    return (p * t * r) / 100

p = float(input("Enter principal: "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))

print("Simple Interest =", simple_interest(p, t, r))