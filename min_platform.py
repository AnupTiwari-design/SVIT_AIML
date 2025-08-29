def min_platforms(arrival, departure):
    n = len(arrival)
    arrival.sort()
    departure.sort()

    plat_needed = 0
    result = 0
    i = 0
    j = 0

    while i < n and j < n:
        if arrival[i] <= departure[j]:
            plat_needed += 1
            result = max(result, plat_needed)
            i += 1
        else:
            plat_needed -= 1
            j += 1

    return result

# Example
arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

print("Minimum Platforms needed:", min_platforms(arrival, departure))