# imports
from turtle import Turtle, Screen
#import another_module

#print(another_module.another_variable)

timmy = Turtle()
print(timmy)

#change the shape
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)

# allow window to continue running until click
my_screen.exitonclick()