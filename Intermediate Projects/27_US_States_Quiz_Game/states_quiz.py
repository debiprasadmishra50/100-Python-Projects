import turtle
import pandas

# set the screen
screen = turtle.Screen()
screen.title("US States Guessing Game")  # Set the screen title

# Create the background image / turtle image
image = "blank_states_img.gif"  # Path to reach the image file
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

"""
# Get the co-ordinates of the states of the screen
# def get_mouse_click_coord(x, y):
#     print(x, y)  # Print the coordinates
#
#
# turtle.onscreenclick(get_mouse_click_coord)  # Call the function each time there is a click
# turtle.mainloop()  # Continue to show the screen even after a click
"""
# OR
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name")
    answer_state = answer_state.title()  # Convert to title case

    # While exiting the game, generate the states to learn
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Check if the answer_state is in the states of all the states of the 50_states.csv
    if answer_state in all_states:
        # If they got it right:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  # get row data
        t.goto(int(state_data.x), int(state_data.y))
        # Create a turtle to write the state name in the relevant coordinates
        t.write(state_data.state.item())
        guessed_states.append(answer_state)
