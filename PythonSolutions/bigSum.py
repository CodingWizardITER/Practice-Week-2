def veryBig(ar):
    sumMin=0
    sumMax=0
    sum=0
    arr=sorted(ar)
    print(list(arr))
    for i in range(5):
        sum+=arr[i]
    print(sum-arr[4],end=" ")
    print(sum-arr[0])


    


    

if __name__=='__main__':
    ar_count=int(input())
    ar=list(map(int,input().rstrip().split()))
    result=veryBig(ar)
    # print(result)