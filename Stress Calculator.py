import tkinter
from tkinter import *
import random


questions = [
    "I have been upset very often due to something that happened unexpectedly ?",
    "I often feel that I'm unable to control important things in my life ?",
    "I often feel stressed out and nervous ?",
    "I often feel confident about my ability to handle my personal problems ?",
    "I often feel that things are going my way ?",
    "I often feel that i am unable to cope with all the things that i have to do ?",
    "I am able to control irritation in my life very often ?",
    "I often feel that I am on top of things ?",
    "I often get angry because of things that happens which are beyond my control ? ",
    "I often feel that difficulties are piling up so high that i cannot overcome them ?",
    "I often get stressed about situations with my friends or family members ?"
    "I often feel that I'm being watched by others and they're gossiping about mes ?"
    
]

answers_choice = [
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],
    ["Strongly disagree"," Disagree"," Neutral"," Agree"," Srongly Agree",],


] 

answers = [0,0,0,6,0,0,0,0,0,0,0,0] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 9):
        x = random.randint(0,10)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score >= 40:
        img = PhotoImage(file="Low Stress.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Excellent Your Stress Is Under Control!!")
    elif (score >= 20 and score < 35):
        img = PhotoImage(file="Moderated Stress Level.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Need 5 Min. break for every 1 Hour !!")
    else:
        img = PhotoImage(file="High Stress.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Very High Level of Stress Detected\nPlease do 1 Hour Yoga on Daily Morning !!")


def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4,r5
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 9:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        r5['text'] = answers_choice[indexes[ques]][4]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4,r5
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)

    r5 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][4],
        font = ("Times", 12),
        value = 4,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r5.pack(pady=5)



def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("Stress Calculator")
root.geometry("1000x800")
root.config(background="#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="Stressed Image.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(10,0))

labeltext = Label(
    root,
    text = "Stress Calculator",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Start Button.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read the Questions Carefully And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text = "This Stress Calculator contains 12 questions\nOnce you select a radio button that will be a final choice\nhence think before you select",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()
