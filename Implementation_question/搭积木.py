import itertools
n,raw,iters,s=int(input()),[],set(),set()
product=list(itertools.product([0,1,2,3,4,5,6],repeat=4))

for _ in range(4):
    raw.append([""]+list(input()))
for a,b,c,d in product:
    iters.add(raw[0][a]+raw[1][b]+raw[2][c]+raw[3][d])
for string in iters:
    tmp=itertools.permutations(list(string))
    for j in tmp:
        s.add("".join(j))

# print(s)
for _ in range(n):print("YES" if input() in s else "NO")