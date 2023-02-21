class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y+other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __call__(self):
        print(f"vector is called")

    def __new__(cls, *args, **kwargs):
        pass


class Person:
    """
    When you create a new object by calling the class, Python calls the __new__()
    method to create the object first and then calls the __init__() method to initialize the object’s attributes.
    Override the __new__() method if you want to tweak the object at creation time.
    """
    def __new__(cls, first_name, last_name):
        # create a new object
        obj = super().__new__(cls)

        # initialize attributes
        obj.first_name = first_name
        obj.last_name = last_name

        # inject new attribute
        obj.full_name = f'{first_name} {last_name}'
        return obj


person = Person('John', 'Doe')
print(person.full_name)

print(person.__dict__)

v1 = Vector(10, 20)
v1()
print(v1.__add__(v1))

