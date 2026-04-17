# Imports
import turtle
import pandas as pd

# setup the screen with the US gif
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Get a prompt


# read the states data
data = pd.read_csv("50_states.csv")

# Get total states
states_list = data.state.to_list()
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                print(state)
        new_data = pd.DataFrame(missing_states)
        #new_data.to_csv("missing_states.csv")
        break
    if answer_state in states_list:
        print("Correct")
        t_name = turtle.Turtle()
        t_name.hideturtle()
        t_name.penup()
        state_data = data[data.state == answer_state]
        # item is used to get the int value, not the dataframe row
        t_name.goto(state_data.x.item(), state_data.y.item())
        t_name.write(answer_state)


# To get the x,y coordinates on the gif
#def get_mouse_click_coor(x, y) -> None:
#    print(x, y)

#turtle.onscreenclick(get_mouse_click_coor)
# REplaces exitonclick so we don't mouse click
#turtle.mainloop()

# Get the screen to exit
screen.exitonclick()