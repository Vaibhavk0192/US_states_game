import turtle as t
import pandas as pd

screen=t.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
t.addshape(image)
t.shape(image)

data=pd.read_csv("50_states.csv")
all__states=data.state.to_list()


guessed_answer=[]


while len(guessed_answer)<50:

    answer=t.textinput(f"{len(guessed_answer)}/50 States Correct","What is another state's name?").title()
    if answer in all__states:
        if answer not in guessed_answer:
            tim=t.Turtle()
            tim.hideturtle()
            tim.penup()
            state_data=data[data.state==answer]
            tim.goto(int(state_data.x),int(state_data.y))
            tim.write(answer)
            guessed_answer.append(answer)
    else:
        pass
        

t.mainloop()
