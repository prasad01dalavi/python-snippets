import myModule             # Import created module
# Note:
# When the module is imported it will run through all the code in mymodule

myModule.simpleFunction1()  # Call a function1 from imported module
myModule.simpleFunction2()  # Call a function2 from imported module

import myModule as m        # Use m instead of the name myModule
m.simpleFunction4()

from myModule import simpleFunction3
simpleFunction3()           # Using function from imported module

from myModule import simpleFunction3 as SF3
SF3()

print 'Import Module Test successful !'
print 'Directories in module =', dir(myModule)


'''
Output:

Other Stuff outside of main module
I am in simple Function 1.
I am in simple Function 2.
I am in simple Function 4.
I am in simple Function 3.
I am in simple Function 3.
Import Module Test successful !
Directories in moduel = ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'simpleFunction1', 'simpleFunction2', 'simpleFunction3', 'simpleFunction4']

'''
