from tkinter import *

root = Tk()
root.title("Simple Calculator") #Title

#Textfield
Textfield = Entry(root, borderwidth=7, width=35)
Textfield.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Define Buttons
button_7 = Button(root, text="7", padx=35, pady=15)
button_8 = Button(root, text="8", padx=35, pady=15)
button_9 = Button(root, text="9", padx=35, pady=15)

button_4 = Button(root, text="4", padx=35, pady=15)
button_5 = Button(root, text="5", padx=35, pady=15)
button_6 = Button(root, text="6", padx=35, pady=15)

button_1 = Button(root, text="1", padx=35, pady=15)
button_2 = Button(root, text="2", padx=35, pady=15)
button_3 = Button(root, text="3", padx=35, pady=15)

button_0 = Button(root, text="0", padx=35, pady=15)

button_divide = Button(root, text="/", padx=35, pady=15)
button_multiply = Button(root, text="*", padx=35, pady=15)
button_minus = Button(root, text="-", padx=35, pady=15)
button_plus = Button(root, text="+", padx=34, pady=15)
button_equals = Button(root, text="=", padx=34, pady=15)

button_clear = Button(root, text="C", padx=35, pady=15)
button_dot = Button(root, text=".", padx=36, pady=15)

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
button_equals.grid(row=5, column=3)

button_clear.grid(row=4, column=0)
button_dot.grid(row=4, column=2)

#Looping
root.mainloop()