from collections import deque


def max_dist(nums):
    if not nums:
        return -1
    left_indices = _find_possible_left_indices(nums)
    right_indices = _find_possible_right_indices(nums)
    i, j = left_indices.popleft(), right_indices.pop()
    current_max_dist = -1
    while True:
        try:
            if nums[i] < nums[j]:
                current_max_dist = max(current_max_dist, j - i)
                j = right_indices.pop()
            else:
                i = left_indices.popleft()
        except IndexError:
            break
    return current_max_dist


def _find_possible_left_indices(nums):
    current_min = float('inf')
    result = deque()
    for i, num in enumerate(nums):
        if num < current_min:
            result.append(i)
            current_min = num
    return result


def _find_possible_right_indices(nums):
    current_max = None
    result_reversed = []
    for j, num in reversed(list(enumerate(nums))):
        if num > current_max:
            result_reversed.append(j)
            current_max = num
    return result_reversed


print max_dist([])
print max_dist([34, 8, 10, 3, 2, 80, 30, 33, 1])
print max_dist([9, 7, 3, 1, 10, 2, 8, 6, 5])
print max_dist([5, 4, 3, 2, 1])
print max_dist([1, 2, 3, 4, 5])
print max_dist([9, 2, 3, 4, 5, 6, 7, 8, 18, 0])
