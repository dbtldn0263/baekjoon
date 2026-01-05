import sys

N=int(sys.stdin.readline())
stack=[]

for i in range(N):
    X=sys.stdin.readline().split()

    if X[0]=='push':
        stack.append(X[1])
    
    elif X[0]=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif X[0]=='size':
        print(len(stack))
    
    elif X[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    
    elif X[0]=='top':
        if stack:
            print(stack[-1])
        else:
            print(-1)