# inheritance: defining classes from classes that have been defined


class Animal:
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("Yum.")


# myanimal = Animal()
# myanimal.who_am_i()

# by passing the Animal class into the Cat class, you now have access
# to the animal methods
class Cat(Animal):
    def __init__(self, name, size):
        # create an instance of Animal when a Cat is created
        Animal.__init__(self)
        self.name = name
        self.size = size

    # if you want to overwrite an existing method, can just define here
    def who_am_i(self):
        print("I am a cat and my name is {}".format(self.name))


mycat = Cat("nubs", "large")
mycat.who_am_i()
mycat.eat()
print(mycat.name)


# polymorphism


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat2:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko = Dog("niko")
felix = Cat2("felix")

# each object has a speak method

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))

# polymorphism example == these are different TYPES of objects but
# the method is named the same

# this doesn't know if you are going to pass in a cat or a dog
# either way - since the method "speak" is named the same, you
# can run them both
def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)

# ex. base class is animal2
class Animal2:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


myanimal = Animal2("fred")
# myanimal.speak() - this provides an error.
# this function requires you to use animal as a SUBCLASS and overwrite
# the function "speak"


class Cat3(Animal2):
    def speak(self):
        return self.name + " says MEOW"


nubs = Cat3("nubs")
print(nubs.speak())

# example: if you wanted to make a base class for opening files -
# you may want to use something like this in order to make sure
# you have appropriately applied formatting for each type
