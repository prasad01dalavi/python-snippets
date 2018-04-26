import re         # Import regular Expression module

result1 = re.split(r'i', 'Python is a Programming Language. I like Python')
print "Result of splitting all i:", result1
# ['Python ', 's a Programm', 'ng Language. I l', 'ke Python']

result2 = re.split(r'i', 'Python is a Programming Language. I like Python',
                   maxsplit=1)
print "Result of maximum one split:", result2
# ['Python ', 's a Programming Language. I like Python']
