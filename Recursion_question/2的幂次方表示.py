from functools import lru_cache
@lru_cache(maxsize=None)
def paw(s:str):
    # s形如"137"
    res=""
    binary=bin(int(s))[1:]
    for i in range(1,len(binary)+1):
        if binary[-i]=='1':
            if i-1<=2 and i-1!=1:
                res='+2({})'.format(i-1)+res
            elif i-1==1:
                res='+2'+res
            else:
                tmp = paw(str(i - 1))
                res='+2({})'.format(tmp)+res
    res=res[1:]
    return res

print(paw(input()))