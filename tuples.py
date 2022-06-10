mytuple = ("Max", 28, "Boston")
print(type(mytuple))

mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

item = mytuple[0]
print(type(item))

for x in mytuple:
    print(x)
if "Max" in mytuple:
    print("yes")
else:
    print("no")

my_tuple = ('a','p','p','l','e')
print(my_tuple.count('p'))
print(my_tuple.index('p'))
my_list = list(my_tuple)
print(my_list)
my_tuple2 = tuple(my_list)
print(my_tuple2)

a=(1,2,3,4,5,6,7,8,9,10)
b = a[2:5]
c = a[4:]
d = a[::2]
e = a[::-1]
print(e)

my_tuple = "Max", 28, "Boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = (0,1,2,3,4)
i1, *i2, i3 = my_tuple
print(i2)