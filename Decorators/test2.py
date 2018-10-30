def decorator_function(original_function): 

    def wrapper_function(args, kwargs):
        print 'I have arguments of original function'
        print 'args:', args
        print 'kwargs:', kwargs
        print 'I can do anything with them and then execute the original function'
        return original_function('Python', 35)
    return wrapper_function


@decorator_function
def display_info(name, age):
    print 'display info function', name, age


display_info('Prasad', 25)
