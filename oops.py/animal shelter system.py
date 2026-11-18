class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        return "..."

    def info(self):
        return f"Animal : {self.name}, Age: {self.age}, Species: {self.species}"

    def __str__(self):
        return f"Animal : {self.name}, Age: {self.age}, Species: {self.species}"

class Pet(Animal):
    def __init__(self, name, age, species, owner_name):
        super().__init__(name, age, species)
        self.owner_name = owner_name 

    def speak(self):
        return f"{self.name} says: Woof!"

    def info(self):
        return f"Pet: {self.name},Owner: {self.owner_name}, Age: {self.age}"

    def __str__(self):
        return f"Pet: {self.name},Owner: {self.owner_name}, Age: {self.age}"

class TrainedPet(Pet):
    def __init__(self, name, age, species, owner_name):
        super().__init__(name, age, species, owner_name)
        self.tricks = []

    def learn_trick(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        tricks = (trick for trick in self.tricks)
        return f"{self.name} knows: {", ".join(tricks)}"

    def info(self):
        return f"TrainedPet: {self.name},Owner: {self.owner_name}, Tricks: {len(self.tricks)}"

    
    def __str__(self):
        return f"TrainedPet: {self.name},Owner: {self.owner_name}, Tricks: {len(self.tricks)}"
    
a = Animal("Tiger", 5, "Cat")
p = Pet("Buddy", 3, "Dog", "Riya")
t = TrainedPet("Max", 2, "Dog", "Nitu")

t.learn_trick("sit")
t.learn_trick("shake")
t.learn_trick("roll over")

print(a)
print(p)
print(t)

print(p.speak())
print(t.speak())
print(t.show_tricks())

print(TrainedPet.__mro__)   




    


