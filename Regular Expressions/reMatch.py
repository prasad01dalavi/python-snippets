import re         #Import regular Expression module
result1 = re.match(r'Python', 'Python is one of the best Programming Language.')
print "Result of finding Python:",result1

#To get the matched word
print "Matched Word:",result1.group(0)

result2 = re.match(r'Programming', 'Python is one of the best Programming Language.')
print "Result of finding Programming:",result2

print "Starting Position of matched word:",result1.start()
print "Ending Position of matched word:",result1.end()

