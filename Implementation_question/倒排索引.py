from collections import defaultdict
# import heapq
words=defaultdict(list)
for i in range(int(input())):
    index=i+1
    file=list(map(str,input().split()))
    for word in set(file[1:]):
        # heapq.heappush(words[word],index)
        words[word].append(index)

for _ in range(int(input())):
    word=input()
    if words[word]:
        print(*sorted(words[word]))
    else:
        print('NOT FOUND')