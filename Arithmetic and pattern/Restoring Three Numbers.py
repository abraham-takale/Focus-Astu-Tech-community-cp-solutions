num=list(map(int,input().split()))
num.sort()
s=num[3]
a=s-num[0]
b=s-num[1]
c=s-num[2]
print(a,b,c)
