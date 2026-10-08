n=int(input())
d=[100,20,10,5,1]
count=0
for coin in d:
    count+=n//coin
    n%=coin
print(count)
