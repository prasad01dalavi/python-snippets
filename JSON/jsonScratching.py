# JSON => Java Script Object Notation
import json

python_string = '''
{"name": "prasad", "age": 24, "language": "python", "positive":  true, "email": null}
'''
json_object = json.loads(python_string)   # python string --> json object
# Converts python string to json object

print json_object
# {u'positive': True, u'age': 24, u'name': u'prasad', u'language': u'python', u'email': None}

print type(json_object)          # <type 'dict'>
print json_object['name']        # prasad

'''
    JSON            python
1. object           dict
2. array            list
3. string           str
4. number(int)      int
5. number(real)     float
6. true             True
7. false            False
8. null             None

'''
# Note the conversion in json_load e.g true -->True, null --> None

del json_object['email']
print json_object
# {u'positive': True, u'age': 24, u'name': u'prasad', u'language': u'python'}

new_string = json.dumps(json_object)    # Json object --> python string
print new_string
# {"positive": true, "age": 24, "name": "prasad", "language": "python"}

print type(new_string)                  # <type 'str'>

new_string = json.dumps(json_object, indent=2)
print new_string
'''
{
  "positive": true,
  "age": 24,
  "name": "prasad",
  "language": "python"
}
'''
