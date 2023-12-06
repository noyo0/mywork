import random
rng = 10
queue = []
for i in range(rng):
    queue.append(random.randint(1,99))
print("queue is", queue)
for b in range(rng):
    print(f"current Number is {queue[0]} and the queue is {queue[1:]}")
    queue.pop(0)
print("the queue is now empty")