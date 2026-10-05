# Dog class

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says wolf!")

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name} turns {self.age}!")

dog_1 = Dog("Charlie", "Golden Retriever", 5)
dog_1.bark()
dog_1.have_birthday()
dog_1.have_birthday()

dog_2 = Dog("Captain", "Pitbull", 10)
dog_2.bark()
dog_2.have_birthday()