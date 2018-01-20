import re         #Import regular Expression module
result1 = re.search(r'Python', 'Python is one of the best Programming Language.')
print "Result of searching Python:",result1

#To get the matched word
print "Matched Word:",result1.group(0)

result2 = re.search(r'Programming', 'Python is one of the best Programming Language.')
print "Result of searching Programming:",result2

print "Starting Position of matched word:",result2.start()
print "Ending Position of matched word:",result2.end()

