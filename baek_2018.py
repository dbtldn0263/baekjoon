N=int(input())
start=1
end=1
total=1
count=0
while start<=N:
    if total<N:
        end=end+1
        total=total+end
        
    elif total>N:
       total=total-start
       start=start+1

    else:
        count=count+1
        total=total-start
        start=start+1
        
print(count)