for i in range(5):
    matrix=list(map(int,input().split()))
    for j in range(5):
        if matrix[j]==1:
            print(abs(i-2)+abs(j-2))
