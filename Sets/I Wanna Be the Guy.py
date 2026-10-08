n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=x[1:] + y[1:]
q=set(z)
if len(q)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
