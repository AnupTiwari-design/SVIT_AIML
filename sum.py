def range_sum(arr, target):
    start = 0
    end = 0
    n = len(arr)
    curr_sum = 0

    while end < n:
        curr_sum += arr[end]

        while curr_sum > target and start <= end:
            curr_sum -= arr[start]
            start += 1

        if curr_sum == target:
            print("Subarray found from index", start, "to", end)
            return

        end += 1

    print("No subarray with given sum found")


arr = [1, 2, 3, 7, 5]
target = 12
range_sum(arr, target)