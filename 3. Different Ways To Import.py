'''
# In Python, you use the import keyword to make code in one module available in another. Imports in Python are
  important for structuring your code effectively. Using imports properly will make you more productive, allowing
  you to reuse code while keeping your projects maintainable.

# There are different ways of using import. Like
--> By using only the module
    import module_name
--> By using function name which are declared in a module to be more explicit.
    import module_name.function_name
--> By using declared package name
    import package_name.module_name / import package_name.module_name.function_name
Or we can use from like
--> from module_name import func1, func2, ....
--> from module_name import *  -- Here * will mean that import everything we have inside that module.
--> from package_name.module_name import finc1, func2, .../ *

# We need to remember that we need to go level by level if we have nested packages.
Let's see some implementation from our previous files.
'''

from utility import multiplication, division
print(multiplication(12,2))
print(division(12,2))
print(max([1,2,3])) # This max will give us the proper output till now.

'''But when we will import our declared max function then it will override the build in function and will provide
an error.
'''
from utility import *
#print(max([1,2,3]))

from Shopping.shopping_cart import *
print(buy('Orange'))

from  Shopping import shopping_cart
print(shopping_cart.buy('Banana'))