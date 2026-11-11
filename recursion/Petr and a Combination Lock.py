t=int(input())
angle=[]
for i in range(t):
    angle.append(int(input()))
def solve(i,total):
    if i==t:
        return total % 360==0
    return (solve(i+1,total+angle[i]) or solve(i+1,total-angle[i]))
if solve(0,0):
    print('YES')
else:
    print('NO') 
    
