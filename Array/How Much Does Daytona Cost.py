n=int(input())
for i in range(n):
    m,k=map(int,input().split())
    num=list(map(int,input().split()))
    if k in num:
        print('YES')
    else:
        print('NO')
