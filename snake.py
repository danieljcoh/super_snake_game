import turtle
from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Snake Class Functions
    def create_snake(self):
        # Setting up the snake and snake length and visibility and starting positions
        for position in STARTING_POSITIONS:
            self.add_snake_segment(position)

    def extend_snake(self):
        self.add_snake_segment(self.segments[-1].position())

    def add_snake_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        # have the squares behind replace their spot with the second to last spot and then move forward
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self):
        # Not the attribute heading. The Turtle.method Heading() which returns a number-of-degrees the turtle is facing.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)