n=int(input())
head=[]
pre=[0]*(n+1)
next=[0]*(n+1)
for i in range(1,n+1):
    pre[i],next[i]=map(int,input().split())

for i in range(1,n+1):
    if pre[i]==0:
        head.append(i)

for i in range(len(head)-1):
    curr=head[i]
    while next[curr]!=0:
        curr=next[curr]
    tail=curr
    next_head=head[i+1]

    next[tail]=next_head
    pre[next_head]=tail
for i in range(1,n+1):
    print(pre[i],next[i])
