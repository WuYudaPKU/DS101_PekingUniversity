from functools import lru_cache
@lru_cache(maxsize=None)
def SierpinskiFractal(n):
    # 该函数的功能是返回边长为n的分型三角形所在矩阵。
    if n==0:
        return [[' ', '/'], ['/', '_'],['\\','_'],[' ','\\']]

    last=SierpinskiFractal(n-1)
    blanks=[[" " for _ in range(int(2**(n)))] for _ in range(2**(n))]

    first_half=blanks+last+blanks
    second_half=last+last
    output=[]
    for col in range(len(first_half)):
        tmp=first_half[col]+second_half[col]
        output.append(tmp)
    return output

def rotate_print(matrix):
    res=[]
    for col in range(len(matrix[0])):
        tmp=""
        for row in range(len(matrix)):
            tmp+=matrix[row][col]
        res.append(tmp)
    for _ in res:
        print(_)
    print('')

while (n:=int(input())) != 0:
    rotate_print(SierpinskiFractal(n))