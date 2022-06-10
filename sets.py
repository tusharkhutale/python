# Sets: unordered, mutable, no duplicates
myset = {1,2,3,1,2}
print(myset)

myset = set([1,2,3])
print(myset)

myset = set("Hello")
print(myset)

myset= {}
myset2 = set()
print(type(myset2))
myset2.add(1)
myset2.add(2)
myset2.add(3)
myset2.remove(3)
myset2.discard(5)
myset2.clear()
print(myset2)

myset = set({1,2,3})
for i in myset:
    print(i)
if 1 in myset:
    print("yes")

# Unions and intersections
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
u = odds.union(evens)
print(u)
i = odds.intersection(evens)
print(i)
i = evens.intersection(primes)
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB)
print(diff)
diff = setB.symmetric_difference(setA)
print(diff)
#setA.update(setB)
#setA.difference_update(setB)
setA.symmetric_difference_update(setB)
print(setA)

setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {7,8}
print(setB.issubset(setA))
print(setA.issuperset(setB))
print(setA.isdisjoint(setC))

setA = {1,2,3,4,5,6}
setB = setA.copy()
setB.add(7)
print(setA)

a = frozenset([1,2,3,4])
#a.add(6)
