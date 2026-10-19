s=input()
num=[]
i=0
while i < len(s):
    if s[i]=='.':
        num.append('0')
        i+=1
    elif s[i]=='-' :
        if s[i+1]=='.':
            num.append('1')
            i+=2
        else :
            num.append('2')
            i+=2
print("".join(num))
