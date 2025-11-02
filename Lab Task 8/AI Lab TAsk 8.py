def minmax(level, node, is_max_turn, nums, max_level):
    if level == max_level:
        return nums[node]

    if is_max_turn:
        left = minmax(level + 1, node * 2, False, nums, max_level)
        right = minmax(level + 1, node * 2 + 1, False, nums, max_level)
        return max(left, right)
    else:
        left = minmax(level + 1, node * 2, True, nums, max_level)
        right = minmax(level + 1, node * 2 + 1, True, nums, max_level)
        return min(left, right)

values = [3, 5, 2, 9, 3, 5, 2, 9]
max_level = 0
n = len(values)
while (2 ** max_level) < n:
    max_level += 1

print("Best value for max player is:", minmax(0, 0, True, values, max_level))
