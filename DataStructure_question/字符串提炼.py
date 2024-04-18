import math
s=input()
n=len(s)
two_int=[int(math.pow(2,i)) \
         for i in range(math.floor(math.log(n,2))+1)]
raw_1=[]
flag_pre=1
flag_rev=-1
while len(raw_1)<len(two_int):
    raw_1.append(s[two_int[flag_pre-1]-1])
    flag_pre+=1
    if len(raw_1)==len(two_int):break
    raw_1.append(s[two_int[flag_rev]-1])
    flag_rev-=1
print("".join(raw_1))