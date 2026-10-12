g=input().upper()
h=input().upper()
letter=input().upper()
pile=g+h
if sorted(letter)==sorted(pile):
    print('YES')
else:
    print('NO')
