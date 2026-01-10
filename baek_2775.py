N=int(input())

for i in range(N):
    k=int(input())
    n=int(input())

    arr=[[0]*(n+1) for x in range(k+1) ]

    for a in range(1,n+1):
        arr[0][a]=a

    for a in range(1,k+1):
        for b in range(1,n+1):
            arr[a][b]=arr[a][b-1]+arr[a-1][b]
    
    print(arr[k][n])