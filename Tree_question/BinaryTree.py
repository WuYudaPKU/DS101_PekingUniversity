# dp=[None for _ in range(10001)]
# dp[1]=(1,1)
# for i in range(2,10000):
#     if i%2==0:
#         dp[i]=(dp[i//2][0]+dp[i//2][1],dp[i//2][1])
#     else:
#         dp[i]=(dp[(i-1)//2][0],dp[(i-1)//2][0]+dp[(i-1)//2][1])
# for i in dp:
#     print(i)

# def paths_cnt(i,j):
#     l_cnt, r_cnt = 0, 0
#     while i!=1 or j!=1:
#         if i>j:
#             l_cnt+=1
#             i-=j
#         else:
#             r_cnt+=1
#             j-=i
#     return l_cnt, r_cnt

'''如果a>b，那么一定有该节点为左子结点，如果其父节点a'>b',那么仍然有其父节点为
左子结点。
问题：何时不是左子结点？
当按照上述操作不断循环左侧-b时，减到a<b为止。
这个次数刚好就是a中有的完整的b的数目，即a//b，接下来变成了a<b的问题，同理可知。
到a,b==1,1递归结束。
'''
def find_path_counts(i, j):
    # 计算向左和向右移动的次数
    left_count = 0
    right_count = 0
    while i != 1 and j != 1:
        if i > j:
            # 计算向左移动的次数
            left_count += i // j
            i %= j
        else:
            # 计算向右移动的次数
            right_count += j // i
            j %= i
    # 如果i或j其中一个为1，则剩下的移动次数为另一个数减1
    if i == 1:
        right_count += j - 1
    else:
        left_count += i - 1
    return left_count, right_count
for i in range(l:=int(input())):
    m,n=map(int,input().split())
    print('Scenario #{}:'.format(i+1))
    print(*find_path_counts(m,n))
    if i!=l-1:print()