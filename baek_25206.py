sm=0
num=0
for _ in range(20):
    name,n,score=input().split()
    n=float(n)

    if score=='P':
        continue

    if score=='A+':
        score_n=4.5
    elif score=='A0':
        score_n=4.0
    elif score=='B+':
        score_n=3.5
    elif score=='B0':
        score_n=3.0
    elif score=='C+':
        score_n=2.5
    elif score=='C0':
        score_n=2.0
    elif score=='D+':
        score_n=1.5
    elif score=='D0':
        score_n=1.0
    elif score=='F':
        score_n=0.0
    
    sm=sm+(score_n*n)
    num=num+n
    
print(sm/num)