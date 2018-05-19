"""
The latest <threading> module provides rich features and greater support for
threads than the legacy <thread> module discussed in the previous section.
The <threading> module is an excellent example of Python Multi-threading.
"""

# Python3
import time
import threading


def calculate_square(number_list):
    print("Calculate Square Function")
    for number in number_list:
        time.sleep(0.2)
        print(f"Square of {number} is {number*number}")


def calculate_cube(number_list):
    print("Calculate Cube Function")
    for number in number_list:
        time.sleep(0.2)
        print(f"Cube of {number} is {number*number*number}")


number_list = [2, 3, 4, 5]
start_time = time.time()
calculate_square(number_list)
print()
calculate_cube(number_list)
print(f"This program took {time.time()-start_time}")  # 1.6000912189483643
print()
# ---------------------------------------------------------------------------- #

# Now by using threading in python3
start_time2 = time.time()
thread1 = threading.Thread(target=calculate_square, args=(number_list,))
# create a thread by giving function name and tuple as argument

thread2 = threading.Thread(target=calculate_cube, args=(number_list,))
# create another thread by giving function name and tuple as argument

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Threading program took {time.time()-start_time2}")
# 0.8060460090637207
