from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")
timmy.color("aquamarine3", "DarkGreen")
timmy.fd(100)
print(timmy)

my_screen = Screen()
print(my_screen.canvheight,my_screen.canvwidth)
my_screen.exitonclick()
