def solve(s,a):
    n=len(s)
    if n==1:
        if s[0]==a:
            return 0
        else:
            return 1
    mid=n//2
    left=s[:mid]
    right=s[mid:]
    left_count=len(left)-left.count(a)
    right_count=len(right)-right.count(a)
    choice1=left_count + solve(right,chr(ord(a)+1))
    choice2=right_count + solve(left,chr(ord(a)+1))
    return min(choice1,choice2)
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    print(solve(s,"a"))
