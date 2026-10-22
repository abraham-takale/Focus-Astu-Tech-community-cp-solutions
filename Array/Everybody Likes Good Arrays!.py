t=int(input())
for i in range(t):
    n=int(input())
    num=list(map(int,input().split()))
    count=0
    for j in range(n-1):
        if (num[j]+num[j+1])%2==0:
            count+=1
    print(count)
