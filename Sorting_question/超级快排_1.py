# 先善用搜索学习逆序数
# 相邻两个数交换，这种排法等价于冒泡排序
# 原问题等价于问冒泡排序最小交换次数
# 冒泡排序中每交换一次逆序对减少一个
# 排n次后逆序对为0，即排序次数=逆序数。

# 对于a,b两个子数组（已经有序），通过双指针把其中元素加入tmp列表中。因为升序所以加入较小的那个，如果较小的在b中，记为b*,则
# 此时a中的所有数字都和b*构成逆序对，逆序对总数+len(a)

# 如果一个数组已经排完，那么他自身内部将不产生逆序对，同时内部的排序不影响他与其他数组产生的逆序对数。
# 因此，我们可以把一个数组拆分成两段，分别求左数组逆序数，右数组逆序数，两数组组合数的逆序数，相加即结果。
res=0
def Merge(a,start,mid,end):
    tmp,l,r,cnt=[],start,mid+1,0
    while l<=mid and r<=end:
        if a[l]<=a[r]:
            tmp.append(a[l])
            l+=1
        else:
            tmp.append(a[r])
            r+=1
            cnt+=mid+1-l
    tmp.extend(a[l:mid+1])
    tmp.extend(a[r:end+1])
    for i in range(start,end+1):
        a[i]=tmp[i-start]
    return cnt

def MergeSort(a,start,end):
    global res
    if start==end:
        return
    mid=(start+end)//2
    MergeSort(a,start,mid)
    MergeSort(a,mid+1,end)
    res+=Merge(a,start,mid,end)


while (n:=int(input()))!=0:
    res,arr=0,[]
    for _ in range(n):
        arr.append(int(input()))
    MergeSort(arr,0,n-1)
    print(res)