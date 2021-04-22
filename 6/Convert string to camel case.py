# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"



def to_camel_case(text):
    text_list = [x for x in text]
    for i in range(len(text_list)):
        if text_list[i].isalpha() == False:
            text_list[i+1] = text_list[i+1].upper()
    
    return "".join([x for x in text_list if x.isalpha()])

print(to_camel_case("The-stealth-warrior"))