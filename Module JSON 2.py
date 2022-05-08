import json

# json to python: loads()
food = '{"fruits":["apple","orange","banana"],"veggies":["palak","gobhi","potato"],"drinks":["water","softdrink","wine"]}'
print(type(food))
items = json.loads(food)
print(items)
print(type(items))
print(items["veggies"])      # now json is working like python dictionary.

# python to json:  dumps()
myitems = {"tv":"samsung","phone":"iphone","car":"None",}
print(type(myitems))
jsn = json.dumps(myitems)
print(jsn)
print(type(jsn))


# reading json file in python: load()
f = open("my intro.json")
jn = json.load(f)
for i,j in jn.items():
    print(i,j)

