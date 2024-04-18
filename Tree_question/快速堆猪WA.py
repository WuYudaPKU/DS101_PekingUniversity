from collections import defaultdict
stack=[]
lo,last_lo=20001,0
dic=defaultdict(int)
while True:
    try:
        tmp=input()
        if tmp=="pop":
            if stack:
                a=stack.pop()
                dic[a]-=1
                if dic[a]==0:
                    lo=last_lo

        elif tmp=="min":
            if len(stack)==0:
                continue
            else:
                print(lo)

        else:
            _,num=map(str,tmp.split())
            num=int(num)   
            stack.append(num)
            dic[num]+=1
            lo=min(num,lo)
            last_lo=lo
    except:
        break