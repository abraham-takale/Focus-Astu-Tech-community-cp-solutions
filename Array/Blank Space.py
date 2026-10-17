t=int(input())
for i in range(t):
    n=int(input())
    count=0
    num=list(map(int,input().split()))
    arr=[]
    for j in range(n):
        if num[j]==0 :
            count+=1
        else:
            arr.append(count)
            count=0
    arr.append(count)
    print(max(arr))
