class Student:
    def __init__(self,id,college):
        self.id = id
        self.college = college
        self.l=[]

    def is_valid(self):
        if not self.l:return False
        self.l.sort()
        self.l.append(10)
        if self.l[0]!=1:return False
        flag=True
        for i in range(len(self.l)-1):
            if self.l[i+1]-self.l[i]>3:
                flag=False
                break
        return flag

from collections import defaultdict
students,colleges,cnt={},defaultdict(int),0
n,m=int(input()),int(input())

for i in range(n):
    id,college=map(int,input().split())
    student=Student(id,college)
    students[id]=student

for i in range(m):
    day,id=map(int,input().split())
    students[id].l.append(day)

for student in students.values():
    if not student.is_valid():
        cnt+=1
        colleges[student.college]+=1

tmp=sorted(colleges.items(),key=lambda x:x[1])
print(cnt)
print(tmp[-1][0])