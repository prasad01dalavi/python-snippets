import mainModule
import mainModule.subModule

mainModule.module1_function()
mainModule.module2_function()

mainModule.subModule.module3_function()
mainModule.subModule.module4_function()
print

mainModule.module1.module1_function()    # calling a method in a module using various methods

from mainModule import module1
module1.module1_function()

from mainModule.module1 import *
module1_function()
