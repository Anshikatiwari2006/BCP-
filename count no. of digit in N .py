n = int(input("Enter a number: "))
count = 1

while n >= 10:
    count += 1
    n //= 10

print("Number of digits:", count)
