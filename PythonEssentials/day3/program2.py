def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True


print("Prime number in range 1-200:")
for i in range(2,201):
    if isPrime(i):
        print(i,end=" ")
        
