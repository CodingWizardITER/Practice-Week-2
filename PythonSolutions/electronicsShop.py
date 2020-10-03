bnm=input().split()
b=int(bnm[0])
n=int(bnm[1])
m=int(bnm[2])
cost=0
keyboards=list(map(int,input().rstrip().split()))
drives=list(map(int,input().rstrip().split()))
max=-1
for i in range(n):
    for j in range(m):
        cost=keyboards[i]+drives[j]
        if(cost>b):
            continue
        elif(cost>max):
            max=cost
print(max)






