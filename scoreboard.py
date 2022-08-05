from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", False, align='left', font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, align='left', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", False, align='center', font=FONT)
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", False, align='left', font=FONT)
