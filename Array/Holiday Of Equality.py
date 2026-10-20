t=int(input())
welfare=list(map(int,input().split()))
burle=0
n=max(welfare)
for i in range(t):
    burle+=n-welfare[i]
print(burle)
