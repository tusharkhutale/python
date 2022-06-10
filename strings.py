# Strings: ordered, immutable, text representation
import time


my_string = 'I\'m a programmer'
my_str = """Hello
World\
welcome"""
print(my_str)

my_string = "Hello World"
char = my_string[3]
print(char)

substring = my_string[1:5]
substring2 = my_string[::2] # every second character
print(substring2)

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)
if 'e' in greeting:
    print('yes')
else:
    print('no')

my_string = '   Hello World      '
my_string = my_string.strip() # remove white spaces from string
print(my_string)
print(my_string.upper()) # upper case
print(my_string.lower()) #lower case
print(my_string.startswith('He')) # check starts with
print(my_string.endswith('ld')) # chck ends with
print(my_string.find('lo')) # return index of found element
print(my_string.replace('World','Universe'))

my_string = 'how are you doing'
my_list = my_string.split()
print(my_list)
my_string = 'how,are,you,doing'
my_list = my_string.split(",")
print(my_list)
new_string = ' '.join(my_list)
print(new_string)

my_list = ['a']*100
#print(my_list)

# bad
my_string = ''
start = time.time()
for i in my_list:
    my_string += i 
#print(my_string)
print(time.time()-start)

# good
my_string = ''
start = time.time()
my_string = ''.join(my_list)
#print(my_string)
print(time.time()-start)

var = "Tom"
my_string = "the variable is %s" % var
print(my_string)
var = 3
my_string = "the variable is %d" % var
print(my_string)
var = 3.1234567
my_string = "the variable is %f" % var
print(my_string)
var = 3.1234567
my_string = "the variable is {}".format(var)
print(my_string)
var = 3.1234567
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var,var2)
print(my_string)
var = 3.1234567
var2 = 6
my_string = f"the variable is {var} and {var2*3}"
print(my_string)