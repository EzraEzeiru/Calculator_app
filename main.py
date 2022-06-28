from tkinter import *

calc_operator = ""

BLACK = "#000000"
GREY = "#D3D3D3"
DARK_GREY = "545454"
DARK_BLUE = "#00008B"

calc_operator = ""


def on_click(text):
    global calc_operator
    calc_operator += str(text)
    entry.insert(END, text)
    text_input.set(calc_operator)


def equals():
    global calc_operator
    temp_op = str(eval(calc_operator))
    entry.delete(0, END)
    entry.insert(0, temp_op)
    text_input.set(temp_op)
    calc_operator = temp_op


def delete():
    global calc_operator
    entry.delete(len(entry.get()) - 1)
    calc_operator = entry.get()
    text_input.set(calc_operator)


def btn_clear():
    global calc_operator
    calc_operator = ""
    text_input.set(calc_operator)
    entry.delete(0, END)


if __name__ == "__main__":
    window = Tk()
    window.title("Calculator App")

    window.resizable(0, 0)

    text_input = StringVar()

    entry = Entry(window, font=('arial', 18, 'bold'), bg=DARK_BLUE)
    entry.grid(row=0, column=0, columnspan=4, ipadx=100, ipady=15, padx=10, pady=10)

    button1 = Button(window, text="1", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click(1))
    button1.grid(column=0, row=1, padx=10, pady=10)

    button2 = Button(window, text="2", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("2"))
    button2.grid(column=1, row=1, padx=10, pady=10)

    button3 = Button(window, text="3", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("3"))
    button3.grid(column=2, row=1, padx=10, pady=10)

    button4 = Button(window, text="4", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("4"))
    button4.grid(column=0, row=2, padx=10, pady=10)

    button5 = Button(window, text="5", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("5"))
    button5.grid(column=1, row=2, padx=10, pady=10)

    button6 = Button(window, text="6", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("6"))
    button6.grid(column=2, row=2, padx=10, pady=10)

    button7 = Button(window, text="7", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("7"))
    button7.grid(column=0, row=3, padx=10, pady=10)

    button8 = Button(window, text="8", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("8"))
    button8.grid(column=1, row=3, padx=10, pady=10)

    button9 = Button(window, text="9", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("9"))
    button9.grid(column=2, row=3, padx=10, pady=10)

    button0 = Button(window, text="0", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("0"))
    button0.grid(column=0, row=4, padx=10, pady=10)

    button_add = Button(window, text="+", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("+"))
    button_add.grid(column=3, row=1, padx=10, pady=10)

    button_subtract = Button(window, text="-", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("-"))
    button_subtract.grid(column=3, row=2, padx=10, pady=10)

    button_multiply = Button(window, text="x", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("*"))
    button_multiply.grid(column=3, row=3, padx=10, pady=10)

    button_divide = Button(window, text="/", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("/"))
    button_divide.grid(column=3, row=4, padx=10, pady=10)

    button_decimal = Button(window, text=".", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=lambda: on_click("."))
    button_decimal.grid(column=1, row=4, padx=10, pady=10)

    button_equals = Button(window, text="=", fg=BLACK, bg=DARK_BLUE, height=1, width=7, border=0, command=equals)
    button_equals.grid(column=2, row=4, padx=10, pady=10)

    button_clear = Button(window, text="C", fg=BLACK, bg=DARK_BLUE, height=2, width=20, border=0, command=btn_clear)
    button_clear.grid(column=2, row=5, columnspan=2, padx=10, pady=10)

    button_delete = Button(window, text="DEL", fg=BLACK, bg=DARK_BLUE, height=2, width=20, border=0, command=delete)
    button_delete.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

    window.mainloop()
