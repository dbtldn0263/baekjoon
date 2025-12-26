N=int(input())

x=[]
x=list(map(int,input().split()))

total=0

for i in range(N):
    k=x[i]/max(x)*100
    total=total+k
print(total/N)