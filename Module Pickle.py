"""
pickle module: whenever we want to serialize and deserialize python objects(all types of datatype) in binary format
we use pickle module.

pickle module contains four methods:
dump() - ye tab use karte hai jab humko object ko pickle(binary format) krke file me store krna hota hai.
dumps() - aur ye tab use krte hai jab humko object ko pickle(binary format) krke as a sting format me change krna hota hai.


load() - ye method tab use krte hai jab pickled object file me store hota hai already aur hume usko unpickle krna hota hai.
loads() - ye method hum tab use krte hai jab koi object already pickled hoke sting k format me hota hai aur humko usko
unpickle krna hota hai.

"""
import pickle

# picking object (changing in binary format)
mydict = {"name":"Rahul Yadav","age":22,"gender":"male","phone":"apple iphone","cars":["audi","mercedes","maruti"]}
pickled_mydict = pickle.dumps(mydict)
print(type(pickled_mydict))
print(pickled_mydict)

# unpickling object (binary formar to readable format)
unpickled = pickle.loads(pickled_mydict)
print(type(unpickled))
print(unpickled)


# now pickling and storing in the file format

file = open("myinfo.pkl","wb")
pickle.dump(mydict,file)
file.close()

# now unpickling the binary object stored in file format

file = open("myinfo.pkl","rb")
mydata = pickle.load(file)
print(mydata)
print(type(mydata))




