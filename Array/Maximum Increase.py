t=int(input())
num=list(map(int,input().split()))
count=1
result=[]
for i in range(t-1):
    if num[i]<num[i+1]:
        count+=1
    elif num[i]>num[i+1] or num[i]==num[i+1] :
        result.append(count)
        count=1
result.append(count)
print(max(result))
