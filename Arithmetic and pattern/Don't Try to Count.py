t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    x=input()
    s=input()
    count=0
    while s not in x and len(x)<n+m-1:
            x+=x
            count+=1
    if s in x:
         print(count)
    else:
        print(-1)
