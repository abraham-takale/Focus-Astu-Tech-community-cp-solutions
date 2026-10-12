n=int(input())
num=list(map(int,input().split()))
odd=[]
even=[]
for i in range(n):
    if num[i]%2==0:
        even.append(i+1)
    else:
        odd.append(i+1)
if len(odd)<len(even):
    print(*odd)
else:
    print(*even)
