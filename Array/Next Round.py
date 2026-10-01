n,k = map(int,input().split())
arr1=list(map(int,input().split()))
count=0
for number in arr1:
    if number >=arr1[k-1] and number>0:
        count+=1
print(count)
