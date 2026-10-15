t=int(input())
for i in range(t):
    num=list(map(int,input().split()))
    num.sort()
    if num[0]==num[1]:
        print(num[2])
    else:
        print(num[0])
