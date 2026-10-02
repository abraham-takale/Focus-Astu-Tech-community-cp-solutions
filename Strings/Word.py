s=input()
up=0
low=0
for cha in s:
    if cha.isupper():
        up+=1
    else:
        low+=1
if up>low:
    print(s.upper())
else:
    print(s.lower())
