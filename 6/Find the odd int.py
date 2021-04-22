# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2 == 1:
#             return i

def find_it(list):
    return [lambda x: list.count(x) % 2 == 1, list]
    # return [x for x in seq if seq.count(x) % 2 == 1][0]

    # [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))