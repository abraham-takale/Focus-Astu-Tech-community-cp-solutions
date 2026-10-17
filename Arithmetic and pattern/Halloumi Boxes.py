t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    num=list(map(int,input().split()))
    s=sorted(num)
    if m==1 and num!=s:
        print('NO')
    else:
        print('YES')
