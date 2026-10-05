s=input().lower()
word='hello'
j=0
for cha in s:
    if j<len(word)and cha == word[j]:
        j+=1
if j==len(word):
    print('YES')
else:
    print('NO')
