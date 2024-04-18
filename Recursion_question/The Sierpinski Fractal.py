from functools import lru_cache
@lru_cache(maxsize=11)
def SierpinskiFractal(n):
    # 该函数的功能是返回边长为n的分型三角形所在矩阵。
    if n==0:
        return [' /\\ ','/__\\']
    last=SierpinskiFractal(n-1)
    width=int(2**(n+2))
    output=[]
    for i in last:
        output.append(" "*((width-len(i))//2)+i+" "*((width-len(i))//2))
    for i in last:
        output.append(i+i)
    return output

while (n:=int(input())) != 0:
    tmp=SierpinskiFractal(n-1)
    for i in tmp:
        print(i)
    print('')