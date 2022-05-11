"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""
""" open() function takes two arguments, one takes 'file name' and other one takes 'mode', mode means in which 
mode we have to open the file"""

f = open("temp.txt")
print(f.read())
f.close()

f=open("temp.txt")
content = f.read(25)
print(content)

f=open("temp.txt","rt")
content = f.read()
print(content)

print(f.readline())

x = open("temp2.txt")
print(x.readline())      #readline() fun read one line at a time.
f.close()

x = open("temp2.txt","rb")    # opening the file in binary mode.
print(x.read())
f.close()

# we can use for loop to iterate the content of file.
x = open("temp2.txt","r")
for i in x:
    print(i)

print("Hello.")
x = open("temp2.txt")    #
print(x.readlines())     # readlines() fun is used to read multiple line in a single list.
x.close()
# TO CREATING A FILE:
t = open("rahuls.txt","w")
t.write("this is rahul who is learning python.")
t = open("rahuls.txt","r")
print(t.read())
t = open("rahuls.txt","a")
t.write("more contents")
t = open("rahuls.txt")
print(t.read())

# TO DELETE THE FIle
import os
os.remove("temp.txt")


