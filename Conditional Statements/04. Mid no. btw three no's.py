#Mid number between three numbers.
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print("Middle number:", a)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print("Middle number:", b)
else:
    print("Middle number:", c)