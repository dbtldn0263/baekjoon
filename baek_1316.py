N=int(input())
count=0

for _ in range(N):
    word=input()
    seen=set()
    bol=True

    for i in range(len(word)):
        if word[i] not in seen:
            seen.add(word[i])

        else:
            if word[i]!=word[i-1]:
                bol=False
                break
    
    if bol:
        count=count+1
        
print(count)