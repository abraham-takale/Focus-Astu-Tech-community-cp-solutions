t=int(input())
for i in range(t):
    s=input()
    x=""
    n=len(s)
    if n>3:
        for j in range(n):
            if j%2!=0:
                x+=s[j]
        print(s[0] + x)
    else:
        print(s)
