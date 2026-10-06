n=int(input())
coins=list(map(int,input().split()))
ord=sorted(coins,reverse=True)
total=sum(coins)
count=0
num=0
for i in range(n):
    if count>total//2:
        break
    else:
        count+=ord[i]
        num+=1
print(num)
