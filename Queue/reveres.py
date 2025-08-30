from collections import deque

def reverse_first_k(queue, k):
    if k <= 0 or k > len(queue):
        return queue
    
    stack = []

    for i in range(k):
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())

    for i in range(len(queue) - k):
        queue.append(queue.popleft())

    return queue


q = deque([10, 20, 30, 40, 50])
k = 3
print("Original Queue:", list(q))
result = reverse_first_k(q, k)
print("After Reversing first", k, "elements:", list(result))