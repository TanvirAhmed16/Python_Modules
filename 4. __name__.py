'''
# Before executing code, Python interpreter reads source file and define few special variables/global variables.
# If the python interpreter is running that module (the source file) as the main program, it sets the special
  __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will
  be set to the module’s name. Module’s name is available as value to __name__ global variable.
# A module is a file containing Python definitions and statements. The file name is the module name with the
  suffix .py appended.
Let's See an example.
'''

print(__name__)
'''
# This file name will be also set to __main__ as we will run this file.
# SO we can use this condition in some points where we  need to.  
'''

# from utility import *
# from Shopping.shopping_cart import *
# if __name__ == '__main__':
#     print(buy('Banana'))
#     print(multiplication(2,3))

# Python program to execute main directly
print("Always executed")

if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported")
