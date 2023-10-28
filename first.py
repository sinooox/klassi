class Human:
    def __init__(self, name, age, height):
        self.setData(name, age, height)
        
    def print(self):
        print(self.name, self.age, self.height)

    def setData(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

p1 = Human('Дэнис', 15, 185)
p1.print()
print("¯\_(ツ)_/¯ "*10)
