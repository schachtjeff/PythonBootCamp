# an args where to sum all values


def add(*args):
    # should be a tuple
    #print(type(args))
    total = 0
    for arg in args:
        total += arg
    return total

# should be 45
print(add(1,2,3,4,5,6,7,8,9))

#unlimited key-word arg
def calculate(n, **kwargs):
    #print(kwargs)
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    #print(kwargs["add"])
    #print(kwargs["multiply"])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.year = kwargs.get('year')

my_car = Car(make='Ford', model='Mustang')
print(my_car.make)
print(my_car.model)
# year becomes None
print(my_car.year)