def sort_str(scales):
    M_part,B_part=[],[]
    for i in scales:
        if i[-1]=="M":
            M_part.append(i)
        elif i[-1]=="B":
            B_part.append(i)
    B_part.sort(key=lambda x:float(x[:len(x)-1]))
    M_part.sort(key=lambda x:float(x[:len(x)-1]))
    return M_part+B_part

from collections import defaultdict
models=defaultdict(list)
for _ in range(n:=int(input())):
    name,scale=map(str,input().split("-"))
    models[name].append(scale)

lst=[]
for name,scales in models.items():
    lst.append((name,scales))
lst.sort(key=lambda x:x[0])
for name,scales in lst:
    print(name+": "+", ".join(sort_str(scales)))