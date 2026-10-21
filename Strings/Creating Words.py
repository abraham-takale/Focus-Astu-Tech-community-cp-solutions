n=int(input())
for i in range(n):
    a,b=input().split()
    c=b[0]+a[1:]
    d=a[0]+b[1:]
    print(c,d)
