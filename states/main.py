
import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_is_on = True

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
all_states_answered = []

while game_is_on:
    answer_state = screen.textinput(title=f"{len(all_states_answered)}/50 States Correct", prompt=f"What's another state's name?").title()
    if answer_state in all_states and answer_state not in all_states_answered:
        print("Correct")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        all_states_answered.append(answer_state)
    elif answer_state in all_states_answered:
        print("Already answered")
    elif answer_state == "Exit":
        missing_states = [state for state in all_states if state not in all_states_answered]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        print("Incorrect")
    if len(all_states_answered) == 50:
        game_is_on = False
        print("You win!")
        congrats = turtle.Turtle()
        congrats.hideturtle()
        congrats.penup()
        congrats.goto(0, 0)
        congrats.write("Congratulations!", align="center", font=("Arial", 24, "normal"))


turtle.mainloop()

