# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

from numpy import char
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

from collections import namedtuple # lightweight object type
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt.x,pt.y)

from collections import OrderedDict 
ordered_dict = OrderedDict()
ordered_dict['d'] = 4
ordered_dict['b'] = 2
ordered_dict['a'] = 1
ordered_dict['c'] = 3
print(ordered_dict)

from collections import defaultdict
#d = defaultdict(int) # for int default value
#d = defaultdict(float) # for float default value
d = defaultdict(list)
d['a'] = 1  
d['b'] = 2
print(d['a'])
print(d['c']) # c is not in d so it print defau;t value of int i.e. 0

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.popleft()
print(d) 
d.extendleft([4,5,6])
print(d)
