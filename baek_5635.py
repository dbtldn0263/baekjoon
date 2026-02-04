N=int(input())
arr=[]
for _ in range(N):
    p,m,d,y=input().split()
    arr.append((p,int(m),int(d),int(y)))

arr.sort(key=lambda x: (x[3],x[2],x[1]),reverse=True)

print(arr[0][0])
print(arr[-1][0])