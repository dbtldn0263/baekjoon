import queue
N=int(input())
num= queue.Queue()

for i in range(1,N+1):
    num.put(i)

while num.qsize() != 1:
    num.get()
    num.put(num.get())

print(num.get())