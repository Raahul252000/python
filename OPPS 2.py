class Employee:
    no_of_leaves = 6   #class variable.
    pass

rahul = Employee()
rohan = Employee()

rahul.name = "Rahul Yadav"
rahul.age = 22
rahul.salary = "95K"
rahul.role = "Software Developer"
rohan.name = "Rohan Sharma"
rohan.age = 25
rohan.salary = "70k"
rohan.role = "Data Analyst"


print(rohan.name)
print(Employee.no_of_leaves)
print(rahul.__dict__)
rahul.no_of_leaves = 8
print(rahul.no_of_leaves)
print(rahul.__dict__)

print(Employee.__dict__)
# we cannot change the class variable with the instance.

Employee.no_of_leaves = 10
print(Employee.__dict__)
print(Employee.no_of_leaves)


