t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int, input().split()))

    freq={}
    ans=0
    for i in range(n):
        key=a[i]-i

        ans+=freq.get(key, 0)
        freq[key]=freq.get(key, 0) + 1
    print(ans)
