n=int(input())
num=list(map(int,input().split()))
a=[]
b=[]
c=[]
for j in range(n):
    if num[j]==1:
        a.append(j+1)
    elif num[j]==2:
        b.append(j+1)
    else:
        c.append(j+1)
w=min(len(a),len(b),len(c))
print(w)
for i in range(w):
    print(a[i],b[i],c[i])
