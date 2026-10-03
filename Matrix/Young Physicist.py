n=int(input())
result=[]
x=0
y=0
z=0
m=0
for j in range(n):
    num=(list(map(int,input().split())))
    result.append(num)
    x+=result[j][m]
    y+=result[j][m+1]
    z+=result[j][m+2]
if x==0 and y==0 and z==0:
    print('YES')
else:
    print('NO')
