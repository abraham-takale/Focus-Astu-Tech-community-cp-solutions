y,w=map(int,input().split())
m=7-max(y,w)
if m==0:
    print('0/1')
elif m==1:
    print('1/6')
elif m==2:
    print('1/3')
elif m==3:
    print('1/2')
elif m==4:
    print('2/3')
elif m==5:
    print('5/6')
elif m==6:
    print('1/1')
