from tkinter import *

root = Tk()
root.title("Simple Calculator") #Title

#Textfield
textfield = Entry(root, borderwidth=7, width=35)
textfield.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Number Function
def button_click(number): 
    current = textfield.get()
    textfield.delete(0, END)
    textfield.insert(0, current + number)

#Delete Function
def button_delete():
    textfield.delete(0, END)

#Plus Function 
def button_addition():
    first = textfield.get()
    global f_first
    f_first = int(first)
    textfield.delete(0, END)

#Equal Function
def button_equal():
    second = textfield.get()
    textfield.delete(0, END)
    textfield.insert(0, f_first + int(second))

#Define Buttons
button_7 = Button(root, text="7", padx=35, pady=15, command=lambda: button_click("7"))
button_8 = Button(root, text="8", padx=35, pady=15, command=lambda: button_click("8"))
button_9 = Button(root, text="9", padx=35, pady=15, command=lambda: button_click("9"))

button_4 = Button(root, text="4", padx=35, pady=15, command=lambda: button_click("4"))
button_5 = Button(root, text="5", padx=35, pady=15, command=lambda: button_click("5"))
button_6 = Button(root, text="6", padx=35, pady=15, command=lambda: button_click("6"))

button_1 = Button(root, text="1", padx=35, pady=15, command=lambda: button_click("1"))
button_2 = Button(root, text="2", padx=35, pady=15, command=lambda: button_click("2"))
button_3 = Button(root, text="3", padx=35, pady=15, command=lambda: button_click("3"))

button_0 = Button(root, text="0", padx=35, pady=15, command=lambda: button_click("0"))

button_divide = Button(root, text="/", padx=35, pady=15)
button_multiply = Button(root, text="*", padx=35, pady=15)
button_minus = Button(root, text="-", padx=35, pady=15)
button_plus = Button(root, text="+", padx=35, pady=15, command=button_addition)
button_equals = Button(root, text="=", padx=165, pady=15, command=button_equal)

button_clear = Button(root, text="C", padx=35, pady=15, command=button_delete)
button_dot = Button(root, text=".", padx=35, pady=15)

#Show Buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_minus.grid(row=3, column=3)
button_plus.grid(row=4, column=3)
button_equals.grid(row=5, column=0, columnspan=4)

button_clear.grid(row=4, column=0)
button_dot.grid(row=4, column=2)

#Looping
root.mainloop()