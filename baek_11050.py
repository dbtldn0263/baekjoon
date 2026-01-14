N,M=map(int,input().split())
n=N
son=1
mom=1
while n!=(N-M):
    son=son*n
    n=n-1

while M!=0:
    mom=mom*M
    M=M-1

print(son//mom)