def maxSequence_fixed(arr):
    sums = []
    for j, e in enumerate(arr):
        sums.append(e)  # <-- HERE
        for i in range(j + 1, len(arr)):
            e += arr[i]
            sums.append(e)
    if all(i<0 for i in arr) or not sums:
        return 0
    else:
        max_sum = max(sums)
        return max_sum