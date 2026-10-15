t=int(input())
for i in range(t):
    num=list(map(int,input().split()))
    count=0
    for i in range(1,4):
        if num[0]<num[i]:
            count+=1
    print(count)
