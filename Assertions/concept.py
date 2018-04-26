"""
An assertion is a sanity-check that you can turn on or turn off
when you are done with your testing of the program.
The easiest way to think of an assertion is to liken it to a raise-if statement
(or to be more accurate, a raise-if-not statement). An expression is tested,
and if the result comes up false, an exception is raised.

Telling the program to test that condition, and trigger an error
if the condition is false.

assert <condition>, <error message>
Similar to the following:

if not condition:
    raise AssertionError()
"""


def num1_greater(num1, num2):
    assert num1 > num2, "Num1 should be always greater"
    print 'Good work!'


num1_greater(5, 2)   # Good work!
num1_greater(5, 12)  # This will create an assertion error

"""
assert num1 > num2, "Num1 should be always greater"
AssertionError: Num1 should be always greater
"""
