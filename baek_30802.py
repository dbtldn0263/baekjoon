import math
N=int(input())
size=list(map(int,input().split()))
T,P=map(int,input().split())
n_sum=0

for i in size:
    num=math.ceil(i/T)
    n_sum=n_sum+num
print (n_sum)
print(N//P,N%P)