"""
Python offers two modules to implement threads in programs:
1. thread
2. threading

The key difference between the two modules is that the module <thread>
implements a thread as a function. On the other hand, the module <threading>
offers an object-oriented approach to enable thread creation.
"""

from thread import start_new_thread
import time


def thread1_function(limit):
    print 'thread1_function is called!'
    print
    
    for count1 in range(limit):
        print 'Count in thread1 is:', count1
        print
        time.sleep(3)
    print '------------ End of Thread 1 --------------'


def thread2_function(limit):
    print 'thread2_function is called!'
    print
    
    for count2 in range(limit):
        print 'Count in thread2 is:', count2
        print
        time.sleep(2)
    print '------------ End of Thread 2 --------------'


start_new_thread(thread1_function, (10, ))   # Arguments will be passed as
start_new_thread(thread2_function, (5, ))    # tuple

print 
print 'After Starting Threads'
print 'Now I will do my tasks'

for cnt in range(1, 20):
    print 'Count, outside of Thread:', cnt
    time.sleep(3)
    print

print 'Completed my external Task!'



