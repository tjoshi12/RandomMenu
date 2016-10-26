from Myro import *
from random import *
list1 = ['spicy', 'creamy', 'mild', 'organic', 'sweet', 'sour', 'hot', 'salty', 'seasoned', 'chile'];
list2 = ['steamed', 'fried', 'sauteed', 'baked', 'grilled', 'sliced', 'marinated', 'scrambled', 'roasted', 'simmered'];
list3 = ['chicken', 'beef', 'pork', 'lamb', 'steak', 'tuna', 'bison', 'noodles', 'venison', 'salmon'];

#for x in range(10):
    #x == 0
    #print(list1[x])
    #x +1
a = 10
b = 10
c = 10

for x in range(10):
    x = randrange(0,a)
    y = randrange(0,b)
    z = randrange(0,c)
    print(list1[x], list2[y], list3[z])
    del list1[x]
    del list2[y]
    del list3[z]
    a = a-1
    b = b-1
    c = c-1
  
