t=int(input())
for i in range(t):
    n=int(input())
    num=sorted(list(map(int,input().split())))
    count1=0
    count2=0
    for j in range(n-1):
        if num[j+1]-num[j]<=1:
            count1=0
        else:
            count2+=1
    if count1!=count2:
        print('NO')
    else:
        print('YES')
