def f(x):
    return int("0b"+x,2)

raw=input()
res=""
for i in range(1,len(raw)+1):
    if f(raw[0:i])%5==0:
        res+="1"
    else:
        res+="0"
print(res)