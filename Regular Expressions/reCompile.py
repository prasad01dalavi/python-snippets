import re         #Import regular Expression module
pattern = re.compile('Python')
#Note that finding is case sensitive
result = pattern.findall('Python is Awesome! I just love Python')
print "Result of Compile:",result
