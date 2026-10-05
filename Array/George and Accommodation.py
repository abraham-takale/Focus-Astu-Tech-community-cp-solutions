n=int(input())
count=0
for i in range(n):
    x,y=map(int,input().split())
    if x+2<=y:
        count+=1
print(count)
