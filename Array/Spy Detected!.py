n=int(input())
for i in range(n):
    m=int(input())
    num=list(map(int,input().split()))
    for i in range(m-2):
        if num[i]!=num[i+1]:
            if num[i+2]==num[i+1]:
                print(i+1)
                break
            else:
                print(i+2)
                break
        
    else:
        print(m)
