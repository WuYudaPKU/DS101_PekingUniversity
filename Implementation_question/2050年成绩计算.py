import math
def is_perfect(x):
    sqrt = math.sqrt(x)
    if sqrt.is_integer():return True
    else:return False
def Euler_sieve(n):
    primes = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes
tuple_primes = tuple(Euler_sieve(10000))
def is_T_primes(x):
    set_1 = set()
    if not is_perfect(x):
        return False
    if x == 4 or x == 9:return True
    elif x == 1:return False
    else:
        a = int(math.sqrt(x))
        tuple_basic = (0, 2, 3, 4)
        if a % 6 in tuple_basic:return False
        else:
            if tuple_primes[a]:return True
            else:return False

m,n=map(int,input().split())
res=[]
for i in range(m):
    temp=list(map(int,input().split()))
    valid=[]
    for j in temp:
        if is_T_primes(j):
            valid.append(j)
    if valid:res.append("{:.2f}".format(sum(valid)/len(temp)))
    else:res.append(0)

for i in res:
    print(i)