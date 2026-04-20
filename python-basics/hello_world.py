# defining var


# assigning single value to variable

my_var = 1
my_next_var = 2

print(my_var)
print(my_next_var)

# assigning single value to variable

my_first_variable = "Now, I'm a string."
print(my_first_variable)

# assigning value to multiple variable

my_var_1, my_var_2, my_var_3 = 1, 2, 3
print(my_var_1, my_var_2, my_var_3)

# my_var_11, my_var_12, my_var_13 = 1
# print(my_var_11, my_var_12, my_var_13) this prints error as rest 2 variables are not assigned value `TypeError: cannot unpack non-iterable int object`

# print type of variable
print(type(my_var))

# defining function in python
def hello():
    return "Hello, World!"

def add_two_num(n1, n2):
    return n1+n2

print(hello())
print(add_two_num(1, 2))

# string literals

str1 = "Amulya"
str2 = 'Kashyap'

print(str1)
print(str2)

# multi line string

mlstr = '''Amulya Kashyap
Is a hero
'''

print(mlstr)