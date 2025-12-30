N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x: (x[1],x[0]))

for j in arr:
    print(j[0],j[1])