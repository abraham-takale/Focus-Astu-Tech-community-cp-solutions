t=int(input())
for i in range(t):
    s="codeforces"
    count=0
    let=input().lower()
    for j in range(10):
       if s[j]!=let[j]:
          count+=1
    print(count)
