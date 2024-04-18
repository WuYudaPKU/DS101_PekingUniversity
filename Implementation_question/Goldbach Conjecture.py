# 23工院 武昱达
def Euler_sieve(n):
    primes = [False]+[True for _ in range(n)]
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    return primes

n=int(input())
l=Euler_sieve(10000)
for i in range(n//2):
    if l[i] and l[n-i]:
        print(i,n-i)
        break