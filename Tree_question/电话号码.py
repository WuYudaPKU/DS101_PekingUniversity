class TrieNode:
    def __init__(self,val):
        self.children = {}
        self.val=val
    def involve(self,s:str):
        if len(s)==1:
            return s in self.children
        if len(s)>=2:
            val=s[0]
            if val in self.children:
                next_node=self.children[val]
                return next_node.involve(s[1:])
            else:return False

    def extend(self,s:str):
        if len(s)==1:
            self.children[s[0]]=s[0]
            return
        elif len(s)>=2:
            self.children[s[0]]=TrieNode(s[0])
            next_node=self.children[s[0]]
            next_node.extend(s[1:])

class Trie:
    def __init__(self):
        self.root=TrieNode(None)

cases=int(input())

for i in range(cases):
    n,trie,flag=int(input()),Trie(),True
    buckets=[[] for _ in range(10)]

    for _ in range(n):
        number=input()
        buckets[int(number[0])].append(number)

    for bucket in buckets:
        bucket.sort(key=lambda x:len(x),reverse=True)
        for num in bucket:
            if not trie.root.involve(num):
                trie.root.extend(num)
            else:
                flag=False
                break
        if not flag:
            break

    print('YES' if flag else "NO")