# [JSON](http://www.json.org/)

### Example Python script returns a boolean if a string is valid json:
import json

def is_json(myjson):  
  try:  
    json_object = json.loads(myjson)  
  except ValueError, e: 
    return False  
  return True 

### Which prints:  

print(is_json("{}"))                          #prints True
print (is_json("{asdf}"))                      #prints False
print (is_json('{ "age":100}'))                #prints True
print (is_json("{'age':100 }"))                #prints False
print (is_json("{\"age\":100 }"))              #prints True
print (is_json('{"age":100 }'))                #prints True
print (is_json('{"foo":[5,6.8],"foo":"bar"}')) #prints True
#Convert a JSON string to a Python dictionary:

import json
mydict = json.loads('{"foo":"bar"}')
print(mydict['foo'])    #prints bar

mylist = json.loads("[5,6,7]")
print(mylist)
[5, 6, 7]
#Convert a python object to JSON string:

foo = {}
foo['gummy'] = 'bear'
print(json.dumps(foo))           #prints {"gummy": "bear"}
#If you want access to low-level parsing, don't roll your own, use an existing library: http://www.json.org/
## Changed remotely
