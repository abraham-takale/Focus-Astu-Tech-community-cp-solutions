n=int(input())
z=[0]
for i in range(n):
    a,b=map(int,input().split())
    x=z[i]-a
    y=x+b
    z.append(y)
print(max(z))
