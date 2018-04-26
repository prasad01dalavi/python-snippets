import re         # Import regular Expression module

pattern = re.compile('Python')
# Similar to findall but it is compiled first

result = pattern.findall('Python is Awesome! I just love Python')
print "Result of Compile:", result
