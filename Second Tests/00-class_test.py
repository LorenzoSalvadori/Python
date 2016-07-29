class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def SayHello(self):
        print("Hello my name is " + self.name)

james = User("James")
fra_gallo = User("FraGallo")
ruggie = User("Ruggero Riccobene")

james.SayHello()
fra_gallo.SayHello()
ruggie.SayHello()