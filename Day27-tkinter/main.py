from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)

input = Entry(width=5)
input.place(x=70, y=50)


miles = Label(text="Miles")
miles.place(x=135, y=50)


def conversion():
    x = int(input.get()) * 1.609
    y = round(x)
    kilometer["text"] = str(y)


convert = Button(text='Calculate', command=conversion)
convert.place(x=53, y=80)


kilometer = Label(text='0')
kilometer.place(x=90,y=110)


miles = Label(text="Kilometers")
miles.place(x=120, y=110)


# Button







window.mainloop()