n,h=map(int,input().split())
W=0
B=0
H=list(map(int,input().split()))
for a in  H:
    if a>h:
        B+=2
    if a<=h:
        W +=1
print(W+B)
