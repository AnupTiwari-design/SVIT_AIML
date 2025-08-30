from collections import deque
# create Queue
queue=deque()

#insert element at queue

queue.append(10)
queue.append(20)
queue.append(30)


print("Queue",list(queue))
print("Dequeued:", queue.popleft())
print("After Dequeue:", list(queue))

# Peek (front element)
print("Front element:", queue[0])

# Size
print("Size:", len(queue))

# Is Empty
print("Is Empty:", len(queue) == 0)
