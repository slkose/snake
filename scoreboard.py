from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
FONT_DOUBLE = ("Courier", 36, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        with open("high_score.txt", mode="r") as h_s:
            self.high_score = int(h_s.read())
        self.board()

    def board(self):
        self.clear()
        self.write(arg=f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as h_s:
                h_s.write(str(self.high_score))
            self.write("NEW HIGH SCORE!\nGAME OVER", align=ALIGNMENT, font=FONT_DOUBLE)
        self.score = 0
        self.board()

    def increase(self):
        self.clear()
        self.score += 1
        self.board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_DOUBLE)
