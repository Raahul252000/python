# Example 2:
class Student:
    def __init__(self,marks):
        self.__marks = marks

    def get_percent(self):
        return (self.__marks/600) * 100

    @property
    def marks(self):
        return f"The marks is {self.__marks}"

    @marks.setter
    def marks(self,value):
        if value < 0 or value > 600:
            print("can't set your value.")
        else:
            print(f"marks is set to {value}")
            self.__marks = value

karan = Student(435)
print(karan.get_percent())
print(karan.marks)

karan.marks = 550
print(karan.get_percent())
print(karan.marks)

