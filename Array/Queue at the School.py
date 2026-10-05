n,t=map(int,input().split())
a=list(input())
for j in range(t):
    i=0
    while i<n-1:
        if a[i]=='B' and a[i+1]=='G':
            a[i],a[i+1]=a[i+1],a[i]
            i+=2
        else:
            i+=1
print("".join(a))
