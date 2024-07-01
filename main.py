from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
is_race_on = False

user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race?")

if user_bet:
    is_race_on = True

colors = ["orange", "violet", "red", "blue", "green", "yellow", "indigo"]
y_positions = [-99, -66, -33, 0, 33, 66, 99]
all_turtle = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

while is_race_on:

    for turtle in all_turtle:

        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print("You Win !!")
            else :
                print(f"You lose. {winning_color} has won the race")

        distance = random.randint(0, 10)
        turtle.forward(distance)





screen.exitonclick()