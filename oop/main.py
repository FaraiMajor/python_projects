class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name +  (self.age)


person1 = MyClass("Farai", "36")

print(person1)
