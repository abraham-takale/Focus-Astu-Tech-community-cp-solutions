n=int(input())
num=list(map(int,input().split()))
mi=n-1-num[::-1].index(min(num))
ma=num.index(max(num))
count=(n-1-mi) +ma
if ma>mi:
    count-=1

print(count)
