n=int(input())
score=list(map(int,input().split()))
max=score[0]
min=score[0]
maxSc=0
minSc=0
for i in range(n):
    if (score[i]>max):
        maxSc+=1
        max=score[i]
    elif(score[i]<min):
        minSc+=1
        min=score[i]
print(maxSc,minSc)