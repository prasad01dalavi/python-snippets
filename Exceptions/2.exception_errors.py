"""
An exception is an error that happens during the execution of a program.
Exceptions are known to non-programmers as instances that do not conform to a
general rule.
"""

try:
    # import unknown_module   # ImportError
    # Uncomment the above line to raise Import Error exception

    # print 1 / 0  # ZeroDivisionError
    # Uncomment the above line to raise ZeroDivisionError

    number = int(raw_input("Enter a number: "))
    print 'Entered Number is:', number

    file_object = open('unnamed_file.txt', 'r')
    print 'File contents are: ', file_object.read()

except ImportError:
    print 'Raised ImportError! An import statement failed.'

except ZeroDivisionError:
    print "Raised ZeroDivisionError! You can't divide by zero, you're silly."

except ValueError:
    print "Raised ValueError! Integer Numbers only"

except IOError:
    print('An error occurred trying to read the file.')

except Exception:
    print 'Some Error Occurred!'

"""
There are number of exception errors. Some of them are listed below:
SyntaxError
SystemError
KeyboardInterrupt
AssertionError
FloatingPointError
OverflowError
"""
