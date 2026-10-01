result=0
n=int(input())
for i in range(n):
    X=input()
    if '++'in X:
        result+=1
    else:
        result-=1
print(result)
