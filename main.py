import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

data_states = pandas.read_csv("50_states.csv")
states_list = data_states.state.to_list()
correct_answers = []

test = turtle.Turtle()
test.hideturtle()
test.penup()

turtle.shape(image)

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/{len(states_list)} States Correct",
                                    prompt="What's another state's name: ").title()
    if answer_state == "Exit":
        break

    if answer_state in states_list:
        data = data_states[data_states.state == answer_state]
        x = int(data.x)
        y = int(data.y)
        test.goto(x, y)
        test.write(f"{answer_state}")
        correct_answers.append(answer_state)

result_list = [i for i in states_list if i not in correct_answers]

data_dict = {
    "States Need To Learn": result_list
}
data_csv = pandas.DataFrame(data_dict)
data_csv.to_csv("learn.csv")
