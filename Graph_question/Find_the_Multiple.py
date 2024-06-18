import itertools
def find_multiple(m):
    for i in range(201):
        for j in itertools.product(*[[0,1] for _ in range(i)]):
            if not j:continue
            num=int("".join(str(k) for k in j))
            if num!=0 and num%m==0:
                return num

while (m:=int(input()))!=0:
    print(find_multiple(m))