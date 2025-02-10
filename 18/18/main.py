from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = {}

# Crear tortugas con nombres únicos y almacenarlas en un diccionario
for index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[index])
    # Usamos el color como nombre único para cada tortuga
    all_turtles[colors[index]] = new_turtle

race_finished = False

while not race_finished:
    for color, turtle in all_turtles.items():
        turtle.forward(randint(0, 10))

        # Comprobar si una tortuga ha cruzado la línea de meta (x > 200)
        if turtle.xcor() > 200:
            race_finished = True
            winning_color = turtle.pencolor()  # Obtener el color de la tortuga ganadora
            print(f"The winner is the {winning_color} turtle!")
            if winning_color == user_bet:
                print("Congratulations! You won the bet!")
            else:
                print(f"Sorry, you lost! The {winning_color} turtle won.")
            break

screen.exitonclick()
