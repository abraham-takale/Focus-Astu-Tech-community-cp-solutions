n=int(input())
l1=['I', 'love', 'that']
l2=['I', 'hate', 'that']
idea=[]
for i in range(1,n+1):
    if i==n:
        l1[2]='it'
        l2[2]='it'
    if i%2==0:
        idea.append(" " .join(l1))
    else:
        idea.append(" " .join(l2))
print(" " .join(idea))
