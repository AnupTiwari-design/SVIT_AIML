from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)  # deque([10, 20, 30])

print("Popped:", stack.pop())   # 30
print("Top:", stack[-1])        # 20
print("Is Empty:", not stack)   # False