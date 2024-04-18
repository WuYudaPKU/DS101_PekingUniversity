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

n=int(input())
lst=list(map(int,input().split()))
lst.reverse()
MergeSort(lst,0,n-1)
print(res)