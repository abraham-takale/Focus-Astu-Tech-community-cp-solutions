n=int(input())
crime=list(map(int,input().split()))
count1=0
count2=0
for event in crime:
    if event==-1:
        if count1>0:
            count1-=1
        else:
            count2+=1
    else:
        count1+=event
print(count2)
