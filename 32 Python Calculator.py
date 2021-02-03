from tkinter import *
import math

root = Tk()
root.geometry("720x600")
root.title("Calculator")

# ################################################# TITLE ##################################################

title = Label(root, text="Calculator", font=('Algerian', 30, 'italic'), fg='Midnightblue', bg='slategray1', height=2)
title.pack(fill=X)

# ################################################# FRAME ##################################################

frame = Frame(root)
frame.pack()

display = PanedWindow(frame)
display.grid(row=0)

button = PanedWindow(frame)
button.grid(row=1)

# ################################################# DISPLAY ##################################################

disLabel = Label(display, text="Enter value Here :  ", font=('Serif', 20), fg='Midnightblue', height=2)
disLabel.grid(row=0, column=0)
entry = Entry(display, width=25, font=('Arial', 27, 'italic'), bd=7)
entry.grid(row=1, column=0, pady=5)

# ################################################# BUTTONS ##################################################

buttonMod = Button(button, text=" % ", font=('Algerian', 20, 'italic'), fg='cyan', bg='gray44', width=5,
                   command=lambda: Click("mod"))
buttonMod.grid(row=0, column=0, padx=3, pady=3)
buttonCE = Button(button, text=" CE ", font=('Algerian', 20, 'italic'), fg='cyan', bg='gray44', width=5)
buttonCE.grid(row=0, column=1, padx=3, pady=3)
buttonC = Button(button, text=" C ", font=('Algerian', 20, 'italic'), fg='cyan', bg='gray44', width=5,
                 command=lambda: Click('C'))
buttonC.grid(row=0, column=2, padx=3, pady=3)
buttonBk = Button(button, text=" <- ", font=('Algerian', 20, 'italic'), fg='cyan', bg='gray44', width=5,
                  command=lambda: Click("<-"))
buttonBk.grid(row=0, column=3, padx=3, pady=3)
buttonDiv = Button(button, text=" / ", font=('Algerian', 20, 'italic'), fg='cyan', bg='gray44', width=5,
                   command=lambda: Click('div'))
buttonDiv.grid(row=0, column=4, padx=3, pady=3)

buttonSqrt = Button(button, text=" ^1/2 ", font=('Algerian', 20, 'italic'), fg='cyan', bg='gray44', width=5,
                    command=lambda: Click("sqrt"))
buttonSqrt.grid(row=1, column=0, padx=3, pady=3)
button7 = Button(button, text=" 7 ", font=('Algerian', 20, 'italic'), fg='cyan', bg='gray44', width=5,
                 command=lambda: Click(7))
button7.grid(row=1, column=1, padx=3, pady=3)
button8 = Button(button, text=" 8 ", font=('Algerian', 20, 'italic'), fg='cyan', bg='gray44', width=5,
                 command=lambda: Click(8))
button8.grid(row=1, column=2, padx=3, pady=3)
button9 = Button(button, text=" 9 ", font=('Algerian', 20, 'italic'), fg='cyan', bg='gray44', width=5,
                 command=lambda: Click(9))
button9.grid(row=1, column=3, padx=3, pady=3)
buttonMul = Button(button, text=" * ", font=('Arial', 20, 'italic'), fg='cyan', bg='gray44', width=5,
                   command=lambda: Click('mul'))
buttonMul.grid(row=1, column=4, padx=3, pady=3)

buttonSqr = Button(button, text = " ^2 ", font = ('Algerian', 20, 'italic'), fg = 'cyan', bg = 'gray44', width = 5,
                   command = lambda : Click("sqr"))
buttonSqr.grid(row = 2, column = 0, padx = 3, pady = 3)
button4 = Button(button, text = " 4 ", font = ('Algerian', 20, 'italic'), fg = 'cyan', bg = 'gray44', width = 5,
                 command = lambda : Click(4))
button4.grid(row = 2, column = 1, padx = 3, pady = 3)
button5 = Button(button, text = " 5 ", font = ('Algerian', 20, 'italic'), fg = 'cyan', bg = 'gray44', width = 5,
                 command = lambda : Click(5))
button5.grid(row = 2, column = 2, padx = 3, pady = 3)
button6 = Button(button, text = " 6 ", font = ('Algerian', 20, 'italic'), fg = 'cyan', bg = 'gray44', width = 5,
                 command = lambda : Click(6))
button6.grid(row = 2, column = 3, padx = 3, pady = 3)
buttonSub = Button(button, text = " - ", font = ('Arial', 20, 'italic'), fg = 'cyan', bg = 'gray44', width = 5,
                   command = lambda : Click('sub'))
buttonSub.grid(row = 2, column = 4, padx = 3, pady = 3)

buttonCube = Button(button, text = " ^3 ", font = ('Algerian', 20, 'italic'), fg = 'cyan', bg = 'gray44', width = 5,
                    command = lambda : Click("cube"))
buttonCube.grid(row = 3, column = 0, padx = 3, pady = 3)
button1 = Button(button, text = " 1 ", font = ('Algerian', 20, 'italic'), fg = 'cyan', bg = 'gray44', width = 5,
                 command = lambda : Click(1))
button1.grid(row = 3, column = 1, padx = 3, pady = 3)
button2 = Button(button, text = " 2 ", font = ('Algerian', 20, 'italic'), fg = 'cyan', bg = 'gray44', width = 5,
                 command = lambda : Click(2))
button2.grid(row = 3, column = 2, padx = 3, pady = 3)
button3 = Button(button, text = " 3 ", font = ('Algerian', 20, 'italic'), fg = 'cyan', bg = 'gray44', width = 5,
                 command = lambda : Click(3))
button3.grid(row = 3, column = 3, padx = 3, pady = 3)
buttonAdd = Button(button, text = " + ", font = ('Arial', 20, 'italic'), fg = 'cyan', bg = 'gray44', width = 5,
                   command = lambda : Click('add'))
buttonAdd.grid(row = 3, column = 4, padx = 3, pady = 3)

buttonDec = Button(button, text = " . ", font = ('Algerian', 20, 'italic'), fg = 'cyan', bg = 'gray44', width = 5,
                   command = lambda : Click('dec'))
buttonDec.grid(row=4, column=0, padx=3, pady=3)
button0 = Button(button, text=" 0 ", font=('Algerian', 20, 'italic'), fg='cyan', bg='gray44', width=11,
                 command=lambda: Click(0))
button0.grid(row=4, column=1, columnspan=2, padx=4, pady=3)
buttonEqual = Button(button, text=" = ", font=('Arial', 20, 'italic'), fg='cyan', bg='gray44', width=12,
                     command=lambda: Click('equal'))
buttonEqual.grid(row=4, column=3, columnspan=2, padx=4, pady=3)


# ################################################# FUNCTION ##################################################

operand = [0]
entry.delete(0, END)


def Click(val):
    if type(val) == int:
        entry.insert(END, val)

    elif val == 'sub' and operand[0] == 0:
        entry.insert(END, '-')

    elif val == 'dec':
        entry.insert(END, '.')

    elif val != 'equal':
        operand.insert(0, float(entry.get()))

        if val == 'add':
            entry.delete(0, END)
            operand.insert(1, 1)

        elif val == 'sub':
            entry.delete(0, END)
            operand.insert(1, 2)

        elif val == 'mul':
            entry.delete(0,END)
            operand.insert(1, 3)

        elif val == 'div':
            entry.delete(0, END)
            operand.insert(1, 4)

        elif val == 'mod':
            entry.delete(0, END)
            operand.insert(1, 5)

        elif val == 'sqrt':
            z = math.sqrt(operand[0])
            entry.delete(0, END)
            entry.insert(END, z)

        elif val == 'sqr':
            z = operand[0] * operand[0]
            entry.delete(0, END)
            entry.insert(END, z)

        elif val == 'cube':
            z = operand[0] * operand[0] * operand[0]
            entry.delete(0, END)
            entry.insert(END, z)

        else:
            entry.delete(0, END)

    else:
        operand.insert(2, float(entry.get()))

        if operand[1] == 1:
            z = operand[0] + operand[2]

        elif operand[1] == 2:
            z = operand[0] - operand[2]

        elif operand[1] == 3:
            z = operand[0] * operand[2]

        elif operand[1] == 4:
            z = operand[0] / operand[2]

        elif operand[1] == 5:
            z = operand[0] % operand[2]

        else:
            z = operand[0] * operand[2] * 0.01

        operand.insert(0, float(entry.get()))
        entry.delete(0, END)
        entry.insert(END, z)


root.mainloop()
