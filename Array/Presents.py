n=int(input())
present=list(map(int,input().split()))
d={}
for i in range(n):
    d[present[i]]=i+1
for i in range(1,n+1):
    print(d[i],end=" ")
