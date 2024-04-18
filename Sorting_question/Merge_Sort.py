# start--mid 和 mid+1--end 都是sorted list
def Merge(a,start,mid,end):
	tmp=[]
	l=start
	r=mid+1
	while l<=mid and r<=end:
		if a[l]<=a[r]:
			tmp.append(a[l])
			l+=1
		else:
			tmp.append(a[r])
			r+=1
	# 以下至少有一个extend了空列表
	tmp.extend(a[l:mid+1])
	tmp.extend(a[r:end+1])
	for i in range(start,end+1):
		a[i]= tmp[i-start]

# 二分
def MergeSort(a,start,end):
	if start==end:
		return

	mid=(start+end)//2
	MergeSort(a,start,mid)
	MergeSort(a,mid+1,end)
	Merge(a,start,mid,end)

a=[8,5,6,4,3,7,10,2]
MergeSort(a,0,7)
print(a)