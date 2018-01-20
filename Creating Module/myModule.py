def simpleFunction1():
    print 'I am in simple Function 1.'


def simpleFunction2():
    print 'I am in simple Function 2.'


def simpleFunction3():
    print 'I am in simple Function 3.'


def simpleFunction4():
    print 'I am in simple Function 4.'


# If I don't want to execute other stuff  while importing the  module I should write this in main
if __name__ == '__main__':
    print "I am in '__name__==__main__' Function"
    print 'Other stuff inside of main that will not be run while importing this module'

print 'Other Stuff outside of main module'
