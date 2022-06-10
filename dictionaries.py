# Dictionary : Key - Value pairs, Unordered, Mutable
mydict = {"name":"Max", "age":28, "city":"New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2) 

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict2["name"])
except:
    print("Error")

for key in mydict:
    print(key)

for key in mydict.keys():
    print(key)

for k in mydict.values():
    print(k)

mydict_cpy = mydict.copy( )
mydict_cpy["email"] = "max@xyz.com"
print(mydict)
print(mydict_cpy)

my_dict = {3:9,6:36,9:81}
print(my_dict)
value = my_dict[3]
print(value)

mytuple = (8,7)
mydict = {mytuple:15}
print(mydict)