t=int(input())
for i in range(t):
    n=int(input())
    num=list(map(int,input().split()))
    print(max(num)-min(num))
