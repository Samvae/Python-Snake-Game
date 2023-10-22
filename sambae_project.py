######################################################################
# Author: Sam Villahermosa
# Username: Samvae
#
# P01: Final Project (Spring 2022)
#
# Purpose: A Python Snake Game

# ######################################################################
# Acknowledgements:
# - Runestone Academy Chapter 15.31 A Programming Example: https://runestone.academy/ns/books/published/csc226-spr22/GUIandEventDrivenProgramming/11_gui_program_example.html
# - Turtle Mainloop: https://stackoverflow.com/questions/38252920/python-turtle-mainloop-usage#:~:text=mainloop()%20is%20a%20function,TurtleScreenBase)%2C%20that%20calls%20TK.
# - Time in python: https://realpython.com/python-sleep/
#
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import turtle
import time
import random

class SnakeGame:
    """
     The class creates the snake, listens to key commands, moves the snake, checks for collision, and tracks the score.
    """
    def __init__(self):
        """
        A constructor for the SnakeGame class
        """
        # Creates Window Screen
        self.wn = turtle.Screen()
        self.wn.title("Snake Game")
        self.wn.bgcolor("white")
        self.wn.setup(600, 600)                                     # Height and Width of the Screen
        self.wn.tracer(0)                                           # Window automatic screen update off

        # Turtle Score Text
        self.text = turtle.Turtle()
        self.text.shape("square")
        self.text.color("gray")
        self.text.penup()
        self.text.hideturtle()
        self.text.goto(0, 250)
        self.text.write("Score : 0  High Score : 0", align="center", font=("consolas", 24, "bold"))

        # Snake head turtle
        self.head = turtle.Turtle()
        self.head.shape("square")
        self.head.color("lime")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "Stop"

        # Food turtle
        self.food = turtle.Turtle()
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0, 100)

        # Listens to key presses
        self.wn.listen()
        self.wn.onkeypress(self.goup, "w")
        self.wn.onkeypress(self.godown, "s")
        self.wn.onkeypress(self.goleft, "a")
        self.wn.onkeypress(self.goright, "d")
        self.wn.onkeypress(self.quit, "q")


    # Assign Key Directions
    def goup(self):
        """
        Checks and sets direction to up
        :return: None
        """
        if self.head.direction != "down":
            self.head.direction = "up"

    def godown(self):
        """
        Checks and sets direction to down.
        :return: None
        """
        if self.head.direction != "up":
            self.head.direction = "down"

    def goleft(self):
        """
        Checks and sets direction to left.
        :return: None
        """
        if self.head.direction != "right":
            self.head.direction = "left"

    def goright(self):
        """
        Checks and sets direction to right
        :return: None
        """
        if self.head.direction != "left":
            self.head.direction = "right"

    def quit(self):
        """
        Closes the game
        :return: None
        """
        if self.head.direction == "Stop":
            self.wn.bye()

    def move(self):
        """
        Moves the snake head 20 units according to the direction
        :return: None
        """
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def gameplay(self):
        """
        Main gameplay of the SnakeGame
        :return: None
        """
        body_part = []                                  # Used to store "parts" of the snake body
        delay = .1                                      # The speed of the game flow
        score = 0
        high_score = 0
        while True:
            self.wn.update()                            # Updates window screen
            if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
                time.sleep(1)
                self.head.goto(0, 0)
                self.head.direction = "Stop"             # Checks for collision with the screen/walls
                for part in body_part:
                    part.goto(1000, 1000)
                body_part.clear()
                score = 0
                delay = 0.1
                self.text.clear()
                self.text.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("consolas", 24, "bold"))
            if self.head.distance(self.food) < 20:         # If head touches food, food goes to a new location
                x = random.randint(-270, 270)
                y = random.randint(-270, 270)
                self.food.goto(x, y)

                # Adding body part of the snake
                new_part = turtle.Turtle()
                new_part.speed(0)
                new_part.shape("square")
                new_part.color("lime")
                new_part.penup()
                body_part.append(new_part)
                delay -= 0.001
                score += 10
                if score > high_score:
                    high_score = score
                self.text.clear()
                self.text.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("consolas", 24, "bold"))
            for index in range(len(body_part) - 1, 0, -1):
                x = body_part[index - 1].xcor()
                y = body_part[index - 1].ycor()
                body_part[index].goto(x, y)
            if len(body_part) > 0:                                  # Body Part follows the head
                x = self.head.xcor()
                y = self.head.ycor()
                body_part[0].goto(x, y)
            self.move()
            for part in body_part:
                if part.distance(self.head) < 20:                   # Checking for head collisions with body parts
                    time.sleep(1)
                    self.head.goto(0, 0)
                    self.head.direction = "stop"
                    for part in body_part:
                        part.goto(1000, 1000)
                    body_part.clear()
                    score = 0
                    delay = 0.1
                    self.text.clear()
                    self.text.write("Score : {} High Score : {} ".format(
                        score, high_score), align="center", font=("consolas", 24, "bold"))
            time.sleep(delay)

def main():
    """
    Runs the class SnakeGame and gameplay
    :return: None
    """
    program = SnakeGame.gameplay(SnakeGame())
    program.wn.mainloop()                                       # Loops the program

main()