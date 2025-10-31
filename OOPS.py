class OOPS:
    eyes = "blue"
    nose = "sharp"
    def eyes_function(self,color):
        print("Eyes function {}".format(color))
    def nose_function(self,size):
        print("Nose function {}".format(size))
    def ears_function(self,color):
        print("Ears function {}".format(color))
pooh = OOPS()
pooh.eyes_function("white")
pooh.nose_function("small")
pooh.ears_function("red")
pooh.eyes_function("yellow")

