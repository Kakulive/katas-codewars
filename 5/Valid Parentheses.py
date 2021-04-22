# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
# Examples

# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

# Constraints

# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

def valid_parentheses(string):
    new_list = []
    for i in string:
        if i == "(":
            new_list.append(i)
        elif i == ")" and len(new_list) != 0:
            new_list.pop()
        elif i == ")" and len(new_list) == 0:
            return False
    
    if len(new_list) == 0:
        return True
    else:
        return False
    
print(valid_parentheses(""))
print(valid_parentheses("hi())"))
print(valid_parentheses("hi(hi)()"))
