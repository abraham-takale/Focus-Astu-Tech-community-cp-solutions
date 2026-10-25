n,k=map(int,input().split())
num=list(map(int,input().split()))
count=0
for i in range(n):
    if num[i]<=5-k:
        count+=1
print(count//3)
