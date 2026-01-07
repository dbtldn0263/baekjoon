N,M=map(int,input().split())

arr=[]
c=64

for i in range(N):
    x=list(input())
    arr.append(x)
 
for j in range(N-7):
    for k in range(M-7):
        w=0
        b=0

        for x in range(j,j+8):
            for y in range(k,k+8):
                if(x+y)%2==0:
                    if arr[x][y]!='W':
                        w=w+1
                    if arr[x][y]!='B':
                        b=b+1
                
                else:
                    if arr[x][y]!='B':
                        w=w+1
                    if arr[x][y]!='W':
                        b=b+1
        
        c=min(c,w,b)
print(c)