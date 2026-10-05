n=int(input())
m=list(map(int,input().split()))
for i in range(n):
    if m[i]==1:
        print('HARD')
        break
else:
    print('EASY')
