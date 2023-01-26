class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

dog1 = Dog("Fido", 3)
dog2 = Dog("Buddy", 5)

dog1.bark() # Output: "Woof!"
dog1.display_info() # Output: "Name: Fido Age: 3"
dog2.display_info() # Output: "Name: Buddy Age: 5"
