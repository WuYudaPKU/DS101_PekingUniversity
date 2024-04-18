# 以十进制转8进制为例
n=int(input())
stack,tmp,res=[],n,""
# n=20
while tmp!=0:
    stack.append(tmp%8)
    tmp=tmp//8
for i in stack:
    res=str(i)+res
print(res)