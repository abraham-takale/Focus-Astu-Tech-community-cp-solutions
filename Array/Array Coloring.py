n=int(input())
for i in  range(n):
    m=int(input())
    num=list(map(int,input().split()))
    odd=0
    even=0
    for j in range(m):
        if num[j]%2==0:
            even+=num[j]
        else:
            odd+=num[j]
    if even%2==0 and odd%2==0:
        print('YES')
    elif even%2!=0 and odd%2!=0:
        print('YES')
    else:
        print('NO')
