f = open("temp1.txt")
# tell() function is used now the position of the file pointer.
print(f.tell())
f.seek(15)
print(f.readline())
print(f.tell())
print(f.readline())
# seek() function is used to
f.seek(8)
print(f.tell())
print(f.readline())
print(f.readlines())
f.close()
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

if os.path.exists("rahul.txt"):
    os.remove("rahul.txt")
else:
    print("no file found.")