# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

#     It must start with a hashtag (#).
#     All words must have their first letter capitalized.
#     If the final result is longer than 140 chars it must return false.
#     If the input or the result is an empty string it must return false.
# Examples

# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

def generate_hashtag(s):
    s_list = s.split(" ")
    s_list_no_spaces = [i for i in s_list if i != ""]

    for i in range (len(s_list_no_spaces)):
        s_list_no_spaces[i] = s_list_no_spaces[i].lower()
        s_list_no_spaces[i] = s_list_no_spaces[i][0].upper() + s_list_no_spaces[i][1:]

    s_list_no_spaces.insert(0,"#")

    if s == "" or len(str(s_list_no_spaces)) > 140:
        return False
    else:
        return "".join(s_list_no_spaces)

print(generate_hashtag("  Hello    Wordl"))
