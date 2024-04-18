from collections import defaultdict

def fill(s:str,n):
    s+='0'*(n-len(s))
    return s

files=defaultdict(str)
# files 形如：“0101010111”
# files[i]存第i个单词出现的文档01串
for word_idx in range(n:=int(input())):
    raw=set(list(map(int,input().split()))[1:])
    for file_idx in raw:
        filled=fill(files[file_idx],word_idx)
        files[file_idx]=filled+'1'

files=sorted(files.items(),key=lambda x:x[0])
for _ in range(M:=int(input())):
    res,appear=[],list(map(int,input().split()))
    for file,judge in files:
        judge,flag=fill(judge,n),True

        for word_idx in range(len(appear)):
            if appear[word_idx]==1 and judge[word_idx]=='0':
                flag=False
                break
            elif appear[word_idx]==-1 and judge[word_idx]=='1':
                flag=False
                break

        if flag:
            res.append(file)

    if res:print(*res)
    else:print('NOT FOUND')