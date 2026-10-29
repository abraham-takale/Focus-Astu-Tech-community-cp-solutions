t=int(input())
for i in range(t):
    n=int(input())
    count=0
    while n!=1:
        if n%6==0:
            n=n//6
            count+=1
        elif (2*n)%6==0:
            n=2*n
            count+=1
        else:
            count=-1
            break
    print(count)
