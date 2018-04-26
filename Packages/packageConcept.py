import mainModule.subModule

mainModule.time.sleep(5)    # Using imported module in __init__.py
# See, Though I have not imported the time module, I could use its function
# Because I imported it in __init__.py

mainModule.module1_function()
# Accessing the module1.py function in mainModule Directory (cool actually)

mainModule.module2_function()
# Accessing the module2.py function in mainModule Directory

mainModule.subModule.module3_function()  # Straight forward but like above case
# Accessing the module3.py function directly in submodule Directory

mainModule.subModule.module4_function()
# Accessing the module4.py function directly
print

mainModule.module1.module1_function()
# calling a function in a module using various methods

from mainModule import module1
module1.module1_function()   # Calling function in module1.py

from mainModule.module1 import *
module1_function()           # Calling function in module1.py
