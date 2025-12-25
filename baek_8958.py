n=int(input())

for i in range(n):
    o=input()
    score=0
    sum=0
    for j in o:
        if j=='O':
            score=score+1
        else:
            score=0
        sum=sum+score
    print(sum)