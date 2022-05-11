class Smartphone:
    display = " full HD"
    def __init__(self,company,model,ram,rom,megapixel):
        self.Company = company
        self.Model = model
        self.Ram = ram
        self.Rom = rom
        self.Camera = megapixel

    def printdetails(self):
        print(f"Your Phone belongs to {self.Company},model is {self.Model},Ram is {self.Ram}, internal memory is {self.Rom} and the Camera is {self.Camera}")

papa = Smartphone("xiaomi","Redmi 9A","4gb","64gb","12 mg")
papa.printdetails()
rahul = Smartphone("xiaome","Redmi note 9 pro","4gb","64 gb","48mg")
print(rahul.Company)
print(rahul.Model)
print(rahul.Ram)
print(rahul.Rom)
print(rahul.Camera)
print(type(rahul))
print(rahul.display)
print(rahul.__dict__)
print(papa.__dict__)


