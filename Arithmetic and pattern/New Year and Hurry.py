n,k=map(int,input().split())
time=240-k
count=0
problem=0
for i in range(1,n+1):
    problem+=5*i
    if time>=problem:
        count+=1
    else:
        break
print(count)
