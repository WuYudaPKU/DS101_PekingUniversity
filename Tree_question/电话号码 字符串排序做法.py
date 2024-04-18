for _ in range(t:=int(input())):
    flag,n=True,int(input())
    numbers=[input() for _ in range(n)]
    numbers.sort()
    for i in range(1,n):
        if numbers[i].startswith(numbers[i-1]):
            flag=False
            break
    print('YES' if flag else 'NO')