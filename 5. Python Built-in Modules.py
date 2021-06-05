'''
# There are tons of Python Built-in modules for us to use. We can easily know about then in the Python Documentation.
https://docs.python.org/3/py-modindex.html
# We don't need to memorise them. Let's see some example of them.
'''

import random
print(random) # We can see where this is stored at.
# We can also use the help function to know what this module does.
#help(random)
# We can see all the methods of that module too...
print(dir(random))

print(random.random()) # This will always a return a random value between 0 to 1.

# We can get an integer value using another module.
print(random.randint(0, 10))
print(random.choice([5,4,3,2,1]))

# We can also be more specific.
from random import shuffle
my_list = ['A','B','C','D','E']
shuffle(my_list)
print(my_list)

# We can also import this modules with differrent names if we face any namre collision. Like...
import random as EDITH
print(EDITH.randint(50, 55))
