n,m,a,b=map(int,input().split())
total=min((n//m)*b +(n%m)*a,n*a,((n+m-1)//m)*b)
print(total)
