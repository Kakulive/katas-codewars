"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""

def solution(s):
    final_list = []
    start_index = 0
    end_index = 2
    
    while end_index < len(s):
        final_list.append(s[start_index:end_index])
        start_index += 2
        end_index += 2
    
    if len(s) % 2 == 1:
        final_list.append(f"{s[-1]}_")

    return final_list

print(solution("asdfadsfa"))

print(list(range(0, 10, 2)))