N=int(input())
human=[]
for i in range(N):
    x,y=map(int,input().split())
    human.append((x,y))

rank=[]
for i in range(N):
    count=0
    for j in range(N):
       if human[i][0]<human[j][0] and human[i][1]<human[j][1]:
           count=count+1
    
    rank.append(count+1)

print(*rank)