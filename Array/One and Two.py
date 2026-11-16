t=int(input())
for i in range(t):
    n=int(input())
    num=list(map(int,input().split()))
    allpro=1
    currpro=1
    for j in range(n):
        allpro *=num[j]
    for k in range(n):
        currpro *= num[k]
        if currpro==allpro//currpro:
            print(k+1)
            break
    else:
        print(-1)
