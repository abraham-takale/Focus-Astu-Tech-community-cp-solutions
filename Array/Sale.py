n,m=map(int,input().split())
num=list(map(int,input().split()))
total=0
num=sorted(num)
for j in range(m):
    if num[j]<0:
        x=abs(num[j])
        total+=x
print(total)
