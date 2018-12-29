# can create your own objects
# uses the "self" keyword - similar to "this"


class NameOfClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    # using "self" to connect this to the actual class it's in
    def some_method(self):
        print(self.param1)


example = NameOfClass("cat", "orange")

example.some_method()


# everything in python is an object
# creating an object of our own, with our own defined .method() information
mylist = [1, 2, 3]


# class - this creates a user defined object
# instance - an object created from a specific class


class Sample:
    pass


potato = Sample()
print(type(potato))
# this prints "__main__.Sample"

# can create attributes for a class


class Dog:

    # to define a class object attribute, or an attribute every
    # instance of a class has - put it here!
    species = "mammal"
    potate = "potato"

    # a special method (a function in an object) is init -- this gets
    # called whenever a new object is created with this class
    def __init__(self, name, size, breed):
        self.name = name
        self.size = size
        self.breed = breed


tina = Dog("tina", "medium", "mix")

print(tina.name + " " + tina.size)

# init is a constructor for the class, and gets called automatically
# whenever you make an instance of the class

# "self" - the specific instance of this class. technically you
# can use whatever word you want

# this __init__ -- THIS is where you pass in the arguments required
# to make the new object

print(tina.name + " " + tina.potate + " " + tina.species)

# methods are functions defined within the object itself
# you can perform actions on an object using a method and the "self" keyword


class Cat:

    # to define a class object attribute, or an attribute every
    # instance of a class has - put it here!
    species = "mammal"
    potate = "potato"

    # a special method (a function in an object) is init -- this gets
    # called whenever a new object is created with this class
    def __init__(self, name, size, breed):
        self.name = name
        self.size = size
        self.breed = breed

    # operations/actions
    # to access self attributes, pass in "self"
    # you MUST pass in self
    def say_hi(self):
        print("{} says MEOW".format(self.name))

    def say_meow(self, n):
        for num in range(0, n):
            print("Meow x {}".format(num + 1))


nubs = Cat("nubs", "large", "mix")

nubs.say_hi()
nubs.say_meow(3)


class Circle:
    # class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def circ(self):
        return 2 * self.pi * self.radius

    def area(self):
        return self.pi * self.radius ** 2


newCirc = Circle(30)
print(newCirc.circ())
