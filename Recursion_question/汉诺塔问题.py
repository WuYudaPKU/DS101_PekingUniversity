def OneMove(x,init,goal):
    print(str(x)+":"+init+"->"+goal)
def Move(num_disks,init,assist,goal):
    if num_disks == 1:
        OneMove(num_disks,init,goal)

    else:
        Move(num_disks-1,init,goal,assist)
        OneMove(num_disks,init,goal)
        Move(num_disks-1,assist,init,goal)

n,a,b,c=map(str,input().split())
Move(int(n),a,b,c)