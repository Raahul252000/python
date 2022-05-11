class Dad:
    sing = 1
    basketball = 1

class Son(Dad):
    dance = 4
    basketball = 3
    def isdance(self):
        return f"yes I dance daily {self.dance} a day. "

class Grandson(Son):
    #dance = 6
    guitar = 10
    basketball = 5
    def isdance(self):
        return f"yes I Properly dance daily {self.dance} a day. "

if __name__ == '__main__':

    sam = Grandson()
    john = Dad()
    mark = Son()
    print(sam.dance)
    print(sam.basketball)
    print(john.basketball)
    print(mark.basketball)

    print(mark.sing)