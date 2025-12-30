words=[]
N=int(input())

for i in range(N):
    words.append(input())

words=list(set(words))

sorted_words=sorted(words,key=lambda x: (len(x),x))

for j in sorted_words:
    print(j)