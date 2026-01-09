from collections import deque
import sys

N=int(sys.stdin.readline())
arr=deque()
for i in range(N):
    x=sys.stdin.readline().split()

    if x[0]=='push':
        arr.append(x[1])
    
    elif x[0]=='pop':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    
    elif x[0]=='size':
        print(len(arr))

    elif x[0]=='empty':
        if len(arr)==0:
            print(1)
        else:
            print(0)
    
    elif x[0]=='front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    
    elif x[0]=='back':
        if arr:
            print(arr[-1])
        else:
            print(-1)
