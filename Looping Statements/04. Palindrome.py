n = int(input("Enter Number: "))
rev = 0
z = n
while n>0:
    rev=(rev*10)+(n%10)
    n=n//10
if rev==z:
    print("Palindrome.")
else:
    print("Not Palindrome.")