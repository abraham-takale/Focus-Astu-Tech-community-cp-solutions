n=int(input())
card=list(map(int,input().split()))
m=n-1
sara=0
dema=0
j=0
while j<m:
    if card[j]<card[m]:
        sara+=card[m]
        m-=1
    else:
        sara+=card[j]
        j+=1
    if card[j]<card[m]:
        dema+=card[m]
        m-=1

    else:
        dema+=card[j]
        j+=1
if n%2!=0:
    sara+=card[j]
print(sara,dema)
