mylist = ["banana", "cherry", "apple"]
print(mylist)

for x in mylist:
    print(x)

if "lemon" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist))

mylist.append("lemon")


mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(mylist)

item = mylist.remove("cherry")
print(mylist)

item = mylist.reverse()
#mylist.clear()
print(mylist)

mylist = [4,2,3,1,-1,-5,10]
mylist.sort()
print(mylist)

mylist = [0] * 5
print(mylist)
mylist2 = [1, 2, 3, 4, 5]
new_list = mylist + mylist2
print(new_list)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
b= mylist[:5]
c = mylist[2:]
d = mylist[::2]
print(d)

list_org = ["banana", "cherry", "apple"]
list_copy = list_org.copy()
list_copy2 = list(list_org)
list_copy.append("lemon")
print(list_org)
print(list_copy2)

a= [1,2,3,4,5,6]
b = [i*i for i in a]
print(a)
print(b)