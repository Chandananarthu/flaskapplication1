number = int(input())

# check if number is greater than 0
if number %2== 0:
    print('Number is even')
else:
    print('number is not even')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
n = int(input())
for i in range(2,n):
    if n%i==0:
        print(n, "is not prime")
        break;
else:
    print(n, "is prime")