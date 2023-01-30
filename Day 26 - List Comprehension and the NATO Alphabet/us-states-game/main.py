import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
FONT = ("Arial", 10, "normal")
ALIGNMENT = "center"

# def get_mouse_click_coor(x, y):
# 	print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
correct_states = 0
correct_guesses = list()


# TODO 4. Use a loop to allow the user to keep guessing
while correct_states < 50:
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct",
                                    prompt="What's another state's name?")
    # TODO 1. Convert the guess to Title Case
    answer_state = answer_state.title()

    # TODO 7. Create a exit
    if answer_state == "Exit":
        break
    # TODO 2. Check if the guess is among the 50 states
    if answer_state in states_list:
        x_coor = data[data.state == answer_state].x.item()
        y_coor = data[data.state == answer_state].y.item()

        # TODO 3. Write correct guesses onto the map
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x=x_coor, y=y_coor)
        new_state.write(answer_state, font=FONT, align=ALIGNMENT)

        # TODO 5. Record the correct guesses in a list
        correct_guesses.append(answer_state)
        print(correct_guesses)

        # TODO 6. Keep track of the score
        correct_states += 1
    else:
        print("False")

# states to learn.csv
state_to_learn = list()
state_to_learn = [state for state in states_list if state not in correct_guesses]

state_to_learn_df = pandas.DataFrame({"Learn": state_to_learn})
state_to_learn_df.to_csv("state_to_learn.csv")
