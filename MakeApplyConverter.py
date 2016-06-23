# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
    return [match, replacement]

def apply_converter(converter, string):
    match = converter[0]
    replacement = converter[1]
    length = len(converter[0])
    while string.find(match) != -1:
        s = string.find(match)
        if s == 0:
            string = replacement + string[length:]
        else:
            string = string[:s] + replacement + string[s + length:]
    return string

def apply_converter2(converter, string):
    prev = None
    while prev != string:
        prev =string
        pos = string.find(convert[0])
        if pos != -1:
            string = string[:pos] + converter[1] + string[pos + len(converter[0]):]
    return string
    
# For example,

c1 = make_converter('aa', 'a')
print(apply_converter(c1, 'aaaa'))
#>>> a

c = make_converter('aba', 'b')
print(apply_converter(c, 'aaaaaabaaaaa'))
#>>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever).
