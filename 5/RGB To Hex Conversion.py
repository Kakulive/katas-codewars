# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    hex_dict = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    rgb_list = [r,g,b]
    for i in range(len(rgb_list)):
        if rgb_list[i]< 0:
            rgb_list[i] = 0
        elif rgb_list[i] > 255:
            rgb_list[i] = 255
    
    hex_list = []
    for i in rgb_list[::-1]:
        if i < 16:
            hex_list.insert(0,"0" + hex_dict[i])
        else:
            while i > 0:
                remainder = i % 16
                hex_list.insert(0,hex_dict[remainder])
                i = (i - remainder) / 16

    return "".join(hex_list)

print(rgb(-20,275,125))
# FEFDFC