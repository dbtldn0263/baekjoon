N,K=map(int,input().split())
arr=[]

for i in range(N):
    arr.append(i+1)

idx=0
result=[]

while len(arr)!=0:
    idx=(idx+K-1)%len(arr)
    result.append(arr.pop(idx))

print("<"+", ".join(map(str,result))+">")