# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

# 'abba' & 'baab' == true

# 'abba' & 'bbaa' == true

# 'abba' & 'abbba' == false

# 'abba' & 'abca' == false

# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words):
    anagram_list = []
    for i in range(len(words)):
        is_the_same = True
        list_of_letters = sorted([x for x in word])
        list_to_check = sorted([x for x in words[i]])
        if len(words[i]) == len(list_of_letters):
            for j in range(len(list_of_letters)):
                if list_of_letters[j] != list_to_check[j]:
                    is_the_same = False
            if is_the_same == True:
                anagram_list.append(words[i])
    
    return anagram_list

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))