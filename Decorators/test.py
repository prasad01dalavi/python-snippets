def decorator_function(original_function): 

    def wrapper_function():
        print 'this is the extra stuff that i want to wrap my original function with'
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print 'Display function ran'


display()
# when this function is run, then the things under the wrapper_function will also be executed
# means we can decorate our original funtion with the things in wrapper function 


