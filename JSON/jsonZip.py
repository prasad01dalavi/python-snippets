##import json
##
##a=[u'kkkjkljl', u'hkjk', u'jkhklj', u'abc', u'hk', u'dfd', u'tyuyt']
##b=["10","5","6"]
##c=['x','y','z']
##
##
##print json.dumps([{'Longitude': country, 'Latitude': wins, 'test': t} for country, wins, t in zip(a, b, c)])


import json

stu = ['abc', 'pqr', 'xyz', 'stu']
team = ['cricket', 'football', 'hollyball', 'cricket']


json_object = json.dumps([{'Student': stu, 'Team': team} for stu, team in zip(stu, team)])
print json_object
