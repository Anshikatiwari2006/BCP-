n = int(input("Enter a number: ")) 
sum = 0

while n > 0:
    n //= 10
    sum = sum+1

print(sum)