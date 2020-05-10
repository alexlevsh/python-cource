class MyObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def instanceMethod(self):
        return print(self.name, 'is', self.age)


alice = MyObject('alice', 21)
alice.instanceMethod()

alex = MyObject('alex', 30)
alex.instanceMethod()
