N,M=map(int,input().split())
num=(list(map(int,input().split())))

num_max=0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            n=num[i]+num[j]+num[k]
            if n<=M and n>num_max:
                num_max=n
print(num_max)