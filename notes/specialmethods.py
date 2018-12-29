# special methods

# if you make your own class, you may not be able to
# read things like "length" or "print"

# in order to use these built-in python methods:
# you use __dunder__ methods


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # if you ever ask for a string definition (i.e. print)
        # return what you want printed
        return "{} by {}. {} pages.".format(self.title, self.author, self.pages)

    def __len__(self):
        # creates the length information
        return self.pages

    def __del__(self):
        # creates something that happens when you delete an instance
        print("A book object has been deleted")


mybook = Book("hi", "ry", 300)

print(mybook)
print(len(mybook))

# to delete an object:
del mybook
