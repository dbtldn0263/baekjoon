arr=[]
for x in range(3):
    arr.append(input())

for y in range(3):
    if arr[y].isdigit():
        i=int(arr[y])+(3-y)
        
if int(i)%3==0 and int(i)%5==0:
    print('FizzBuzz')

elif int(i)%3==0 and not int(i)%5==0:
    print('Fizz')

elif int(i)%5==0 and not int(i)%3==0:
    print('Buzz')

else:
    print(i)
