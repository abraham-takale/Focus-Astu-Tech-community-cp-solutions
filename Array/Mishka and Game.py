r=int(input())
m1=0
c1=0
for i in range(r):
    m,c=map(int,input().split())
    if m>c:
        m1+=1
    elif m<c:
        c1+=1
if m1>c1:
    print("Mishka")
elif m1<c1:
    print('Chris')
else:
    print('Friendship is magic!^^')
