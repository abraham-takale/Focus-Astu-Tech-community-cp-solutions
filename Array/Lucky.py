t=int(input())
for i in range(t):
    n=input()
    num=list(map(int,n))
    m=len(num)
    if sum(num[:m//2])==sum(num[m//2:]):
        print('YES')
    else:
        print('NO')
