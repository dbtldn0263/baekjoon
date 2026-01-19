N=int(input())
count=0
i=5

while N//i>=1:
    count=count+(N//i)

    i=i*5

print(count)