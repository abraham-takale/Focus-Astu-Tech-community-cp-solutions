n=int(input())
progress=list(map(int,input().split()))
result=[]
count=1
for i in range(n-1):
    if progress[i]<=progress[i+1]:
        count+=1
    else:
        result.append(count)
        count=1
result.append(count)
print(max(result))
