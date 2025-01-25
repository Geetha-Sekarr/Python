class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} meows.")

dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", breed="Siamese")

dog.speak()  
cat.speak()  

print(f"{dog.name} is a {dog.species}.")  
print(f"{cat.name} is a {cat.species}.")  
