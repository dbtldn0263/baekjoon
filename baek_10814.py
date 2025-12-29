people=[]
N=int(input())

for i in range(N):
    person=input().split()
    people.append(person)

people.sort(key=lambda x: int(x[0]))

for age,name in people:
    print(age,name)