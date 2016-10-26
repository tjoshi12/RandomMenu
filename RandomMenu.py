from Myro import *
from random import *
list1 = ['spicy', 'creamy', 'mild', 'organic', 'sweet', 'sour', 'hot', 'salty', 'seasoned', 'chile'];
list2 = ['steamed', 'fried', 'sauteed', 'baked', 'grilled', 'sliced', 'marinated', 'scrambled', 'roasted', 'simmered'];
list3 = ['chicken', 'beef', 'pork', 'lamb', 'steak', 'tuna', 'bison', 'noodles', 'venison', 'salmon'];

print("Welcome to Tej's restaurant!")
print("Here is our menu for tonight:")

list1range = 10
list2range = 10
list3range = 10

for x in range(10):
    adjective = randrange(0,list1range)
    verb = randrange(0,list2range)
    noun = randrange(0,list3range)
    print(list1[adjective], list2[verb], list3[noun])
    del list1[adjective]
    del list2[verb]
    del list3[noun]
    list1range = list1range -1
    list2range = list2range -1
    list3range = list3range -1
  
