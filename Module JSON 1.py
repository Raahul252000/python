"""
JSON  (JavaScript Object Notation) is a file that is mainly used to store and transfer data mostly between
a server and a web application. It is popularly used for representing structured data. In this article, we will discuss
how to handle JSON data using Python. Python provides a module called json which comes with Python’s standard
built-in utility.
 We can import json module by using the import statement.

Parse JSON - Convert from JSON to Python:
If you have a JSON string, you can parse it by using the json.loads() method.
The result will be a Python dictionary.
"""
import json
mydata = '{"name":"rahul","gender":"male"}'
print(type(mydata))

parsed = json.loads(mydata)        # we can parsed the json string using load function. this will convert the string into dictionary.
print(parsed)
print(type(parsed))
print(parsed["name"])
print(parsed["gender"])

mydata2 = {"name":"rahul Yadav","qualification":"MCA","cars":["audi","mercedes","bmw"],"Phone":"iphone"}
print(type(mydata2))
print(mydata2)

a = json.dumps(mydata2)             # we can use dumps() to convert python to json.
print(type(a))
print(a)

"""
Python objects and their equivalent conversion to JSON:

Python = JSON Equivalent
dict = object
list, tuple = array
str = string
int, float = number
True = true
False = false
None = null
"""

list1 = ["apple","orange","banana","grapes"]
print(type(list1))

jsn = json.dumps(list1)
print(type(jsn))
print(jsn)

# Reading json file in python:

f = open("my intro.json")
data = json.load(f)
print(f)


