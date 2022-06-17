import json

# json to python: loads()
"""
when we simply just want to convert the json object into python object then loads() function is used.
"""

food = '{"fruits":["apple","orange"],"veggies":["palak","gobhi"],"drinks":["water","softdrink"]}'
print(type(food))
items = json.loads(food)
print(items)
print(type(items))
print(items["veggies"])      # now json is working like python dictionary.

# python to json:  dumps()
"""
when we simply just want to convert python object into json object then dumps() function is used.
"""
myitems = {"tv":"samsung","phone":"iphone","car":"i20",}
print(type(myitems))
jsn = json.dumps(myitems)
print(jsn)
print(type(jsn))


# reading json file in python: load()
"""
But when we want to read the json data from the json file then we use load() function. it first converts the json object
into python object from the json file and after that we can read it.
"""
f = open("mydata.json","r")
jn = json.load(f)
for i,j in jn.items():
    print(i,j)

# write to JSON file.
"""
if we directly want to convert python object into json object and along with that we want write it into json file then we
use 'dump()' function.
"""

mydict = {"Name":"Rahul Yadav","Age": 22,"Gender":"Male","role": "SDE"}
with open("mydata.json","a") as json_obj:
     json.dump(mydict,json_obj)
