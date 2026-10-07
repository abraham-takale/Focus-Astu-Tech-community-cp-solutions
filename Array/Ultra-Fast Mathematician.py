n=input()
m=input()
result=[]
for i in range(len(n)):
    if n[i]==m[i]:
        result.append('0')
    else:
        result.append('1')
print( "".join(result))
