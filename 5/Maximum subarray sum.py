# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]

# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

# import copy

# def max_sequence(arr):
#     negative_check = 0
#     for element in arr:
#         if element < 0:
#             negative_check += 1
    
#     if negative_check == len(arr):
#         return 0

#     sum_arr = sum(arr)
#     control = 1
#     backup_array = copy.deepcopy(arr) 
#     for i in range(len(arr)):
#         for i in range(len(arr)):
#             if sum_arr < sum(arr):
#                 sum_arr = sum(arr)
#             arr.pop()
#         arr = copy.deepcopy(backup_array)[control:]
#         control += 1
#     return sum_arr

def max_sequence(arr):
    if len(arr) == 0 or max(arr) < 0:
        return 0
    m = arr[0]
    current = arr[0]
    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        m = max(m, current)

    return m


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))