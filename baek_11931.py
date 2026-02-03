import sys
input=sys.stdin.readline
N=int(input())
arr=[]
for _ in range(N):
    x=int(input())
    arr.append(x)
arr.sort(reverse=True)

for i in arr:
    print(i)