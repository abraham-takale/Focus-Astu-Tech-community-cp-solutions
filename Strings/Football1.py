t=int(input())
te1=input()
count1=1
count2=0
for i in range(t-1):
    te2=input()
    if te1==te2:
        count1+=1
    else:
        count2+=1
        te=te2
if count1>count2:
    print(te1)
else:
    print(te)
