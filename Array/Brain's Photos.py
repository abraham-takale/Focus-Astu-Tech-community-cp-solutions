n,m=map(int,input().split())
che1=['C','M','Y']
che2=['W','G','B']
count=0
for i in range(n):
    cha=list(map(str,input().split()))
    for j in range(m):
        if cha[j] in che2:
            count+=1
if count==n*m:
    print("#Black&White")
else:
    print("#Color")
