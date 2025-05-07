import turtle as t
import pandas as pd


FONT = ("Courier", 12, "normal")

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
data_states = pd.read_csv('50_states.csv')
state = data_states['state'].to_list()
# print(state)

turt = t.Turtle()

screen.addshape(image)
t.shape(image)

guesses = []


# print(answer_state)
game_is_on = True
while game_is_on:
    if len(guesses) == 0:
        text = "Guess a state"
    else:
        text = "What another state's name?"
    answer_state = screen.textinput(title=f"{len(guesses)}/{len(state)} States Correct", prompt=text).title()
    if answer_state == "Exit":
        missing_states = [a_state for a_state in state if a_state not in guesses]
        # for a_state in state:
        #     if a_state not in guesses:
        #         missing_states.append(a_state)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False
    if answer_state in state:
        turt.penup()
        turt.hideturtle()
        data_position = data_states[data_states['state'] == answer_state]
        x_position = (data_position['x'].to_list())[0]
        y_position = (data_position['y'].to_list())[0]
        turt.goto(x_position, y_position)
        turt.write(arg=answer_state,align='center',font=FONT)
        guesses.append(answer_state)
    if len(guesses) == 50:
        game_is_on = False


## item() --> to get data without index

# for a_state in state:
#         if a_state not in guesses:
#             with open("./states_to_learn.csv", 'a') as miss_state_file:
#                 miss_state_file.write(f"{a_state}\n")



# def get_mouse_click_cor(x, y):
#     print(x, y)
#self.write(f" Level: {self.level}", align="center",font=FONT)
# t.onscreenclick(get_mouse_click_cor)
#
# t.mainloop()


# screen.exitonclick()

