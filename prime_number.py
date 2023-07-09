n = int(input())
# lesser than 2 is not prime numbers
if n < 2:
    print("NO")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0: # if it can be divided by another num its not prime
            is_prime = False
            break
    
    if is_prime:
        print("YES")
    else:
        print("NO")
