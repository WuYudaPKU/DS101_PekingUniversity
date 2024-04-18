import math
a1,a2,b1,b2=map(int,input().split())
temp1=a1*b2+b1*a2
temp2=a2*b2
a=math.gcd(temp1,temp2)
print(str(temp1//a)+"/"+str(temp2//a))