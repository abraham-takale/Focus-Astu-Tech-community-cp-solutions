t=int(input())
for i in range(t):
    n=int(input())
    num=input()
    i=0
    j=n-1
    count=0
    while i<j:
        if num[i]!=num[j]:
            count+=2
            i+=1
            j-=1
        else:
            break
    print(abs(n-count))
