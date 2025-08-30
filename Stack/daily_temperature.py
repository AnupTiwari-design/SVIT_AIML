def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []  # stores indices

    for i, temp in enumerate(temperatures):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)

    return answer

# Example
temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temps))