class Student:
    def __init__(self,id,l:list):
        self.id = id
        self.l=l
    def _GPA_credit(self):
        lst=[]
        for score,credit in self.l:
            if score<60:lst.append((0,credit))
            else:lst.append((4-3*(100-score)**2/1600,credit))
        return lst
    def GPA(self):
        lst=self._GPA_credit()
        return sum(i*j for i,j in lst)/sum(j[1] for j in lst)


N,M=map(int,input().split())
students,accepted=[],[]
for _ in range(N):
    info = list(map(int, input().split()))
    l = [(info[i], info[i + 1]) for i in range(1, len(info[1:]), 2)]
    students.append(Student(info[0],l))
students.sort(key=lambda x:x.GPA())
for i in range(M):
    accepted.append(students.pop().id)
print(*accepted)