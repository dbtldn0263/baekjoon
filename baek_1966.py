n=int(input())

for _ in range(n):
    N,M=map(int,input().split())
    imp=list(map(int,input().split()))
    
    q=[]
    
    for i in range(N):
       q.append((imp[i],i))

    count=0

    while True:
        cur=q.pop(0)

        bl=False

        for x in q:
            if cur[0]<x[0]:
                bl=True
                break

        if bl:
            q.append(cur)
            
        else:
            count=count+1

            if cur[1]==M:
                print(count)
                break