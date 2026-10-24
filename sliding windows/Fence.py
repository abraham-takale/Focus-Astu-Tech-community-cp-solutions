n,k =map(int,input().split())
h=list(map(int,input().split()))
pre=sum(h[:k])
s=pre
j=0
for i in range(k,n):
    s=s-h[i-k]+h[i]
    if pre>s:
        pre=s
        j=i-k+1
print(j+1)
