from collections import deque
def generate_binary_numbers(n):
    result = []
    q = deque()

    # Start with "1"
    q.append("1")

    # Generate numbers
    for i in range(n):
        curr = q.popleft()
        result.append(curr)

        # Append next two binary numbers
        q.append(curr + "0")
        q.append(curr + "1")

    return result

# Example usage
n = 5
print(generate_binary_numbers(n))