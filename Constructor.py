class Practice:
    def __init__(self, name ,id):
        print("inside constructor")
        self.name = name
        self.id = id
    def printname(self):
        print("inside printname",self.name)
        print("inside printage",self.id)



    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    # def test(self):
    #     print("Hello " + self.name + "!")
    #     print("Age is: " + str(self.age))
    # practo = Practice()
    # practo.test()
practo = Practice("practo",1)
practo.printname()