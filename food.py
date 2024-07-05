from turtle import Turtle
import random

class Food(Turtle):  #that way inherits turtle things so can interact on screen
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup() #so when it moves across the map doesnt leave a line
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #to make it smaller, usually 20 now half 10
        self.color("blue") #change color
        self.speed("fastest") #so we dont see it move on the map
        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 280)
        # self.goto(random_x, random_y)
        self.change_position()

    def change_position(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

