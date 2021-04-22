# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

# def move_zeros(array):
#     zero_counter = 0
#     for i in array:
#         if i == 0:
#             zero_counter += 1
#     for i in range(zero_counter):
#         array.remove(0)
#     for i in range(zero_counter):
#         array.append(0)

#     return array

def move_zeros(arr):
    non_zeros = []
    zeros = []
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros.append(0)
        else:
            non_zeros.append(arr[i])

    return non_zeros+zeros

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))