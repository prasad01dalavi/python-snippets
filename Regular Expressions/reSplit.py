import re         #Import regular Expression module
result1 = re.split(r'i', 'Python is a Programming Language. I like Python')
print "Result of splitting all i:",result1

result2 = re.split(r'i','Python is a Programming Language. I like Python',maxsplit=1)
print "Result of maximum one split:",result2
