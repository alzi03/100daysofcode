from tkinter import *
import time
from playsound import playsound


# Setting up main window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg='#cbbeb5')

# Adding Title + Number of Cycles

title = Label(text=f'Pomodoro', bg='#cbbeb5', font=('Roboto', 42, 'bold'), fg='Black')
title.pack()

#  Adding the tomato image + timer
canvas = Canvas(width=210, height=224, bg='#cbbeb5', highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(103, 112, image=tomato)
canvas.pack()

timer = Label(text='20:00')
timer.config(bg='#cbbeb5', fg='Black', font=('Roboto', 24, 'bold'))
timer.pack()


# Timer Countdown
def alarm():
    playsound('alarm.wav')


def formatting(x, y):  # ensures proper time formatting
    x, y = str(x), str(y)
    if len(x) == 1: x = '0' + str(x)
    if len(y) == 1: y = '0' + str(y)
    return (x, y)


def counting(worktime):  # countdown clock
    mins, secs = divmod(worktime, 60)
    mins, secs = formatting(mins, secs)
    timer["text"] = f'{mins}:{secs}'
    window.update()
    time.sleep(1)


# How manny full pomodoro cycles
cycles = 0

numcycles = Label(text=f'# of Cycles: {cycles}')
numcycles.config(bg='#cbbeb5', fg= 'Black', font=('Roboto', 10, 'bold'))
numcycles.pack()

# 20 minutes worktime, 5 minutes break, activated each time on start button
def countdown():
    global cycles
    worktime = 1200
    while worktime != 0:
        worktime -= 1
        counting(worktime)
        if timer['text'] == '20:00':
            return
    alarm()
    timer['text'] = '05:00'
    worktime = 300
    while worktime != 0:
        worktime -= 1
        counting(worktime)
    alarm()
    cycles += 1
    numcycles['text'] = f'# of cycles: {cycles}'
    resetter()


# reset button brings the timer back to 20:00, doesn't count cycle as one complete
def resetter():
    timer["text"] = '20:00'


# start and reset buttons, commands above ^
start = Button(command=countdown)
start.config(text='Start', bg='#cbbeb5')
start.place(x=-25, y=350)

reset = Button(command=resetter)
reset.config(text='Reset', bg='#cbbeb5')
reset.place(x=175, y=350)


window.mainloop()



