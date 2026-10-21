n=input()
invert=[]
for i in range(len(n)):
    m=int(n[i])
    if i==0 and m==9:
        invert.append('9')
    else:
        invert.append(str(min(m,9-m)))
print("".join(invert))
