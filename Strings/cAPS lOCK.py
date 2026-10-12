s=input()
if s==s.upper() or s==s[0].lower()+s[1:].upper():
    print(s.swapcase())
else:
    print(s)
