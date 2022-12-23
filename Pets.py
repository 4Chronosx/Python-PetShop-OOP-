class Animal:
    def __init__(self, name, species, price):
        self.name = name
        self.species = species
        self.price = price

    def make_sound(self, sound):
        print(sound)

    def do_action(self, action):
        print(action)


class Dog(Animal):
    def __init__(self, name, species, price, breed, tail):
        super().__init__(name, species, price)
        self.breed = breed
        self.tail = tail

    def bark(self):
        self.make_sound("Woof!")

    def fetch(self):
        self.do_action(self.name + " is fetching")


class Cat(Animal):
    def __init__(self, name, species, price, breed, whiskers):
        super().__init__(name, species, price)
        self.breed = breed
        self.whiskers = whiskers

    def meow(self):
        self.make_sound("Meow!")

    def fetch(self):
        self.do_action(self.name + " is stalking")


class Fish(Animal):
    def __init__(self, name, species, price, breed, fins):
        super().__init__(name, species, price)
        self.breed = breed
        self.fins = fins

    def blub(self):
        self.make_sound("blub!")

    def swim(self):
        self.do_action(self.name + " is swimming")


#honey = Dog("Honey", "Dog", 5000, "Shitzu Poodle", True)
#honey.bark()
#honey.fetch()

#nemo = Fish("Nemo", "Fish", 1000, "Gold Fish", True)
#nemo.blub()
#nemo.swim()




