n=int(input())
data={}
for i in range(n):
    name=input()
    if name not in data:
        print('OK')
        data[name]=1
    else:
        print(name + str(data[name]))
        data[name]+=1
