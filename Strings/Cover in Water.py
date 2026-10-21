t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    count=0
    if '...' in s:
        print(2)
    else:
        print(s.count('.'))
