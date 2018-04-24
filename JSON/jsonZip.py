import json

key_list = ['key1', 'key2', 'key3']
value_list = ['value1', 'value2', 'value3']

my_dict = dict(zip(key_list, value_list))
print my_dict
# {'key3': 'value3', 'key2': 'value2', 'key1': 'value1'}

python_string = json.dumps(my_dict)   # Json object --> python string
print python_string, type(python_string)
# {"key3": "value3", "key2": "value2", "key1": "value1"} <type 'str'>
