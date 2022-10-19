from tkinter import *

root = Tk()
root.title('My calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Functions for the buttons like our additions and equations buttons

def user_choice():
    return

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def button_minus():
    first_number = e.get()
    global f_num
    global math
    math = 'minus'
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'times'
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'divides'
    f_num = int(first_number)
    e.delete(0, END)

def button_clear():
    e.delete(0, END)

#future iteration will actually have the backspace... you know, work... 
def button_backspace():
    remove_last = e.get()[:-1]
    e.delete(remove_last)
    

def equate():
    second_number = e.get()
    e.delete(0, END)

    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    if math == 'minus':
        e.insert(0, f_num - int(second_number))
    if math == 'times':
        e.insert(0, f_num * int(second_number))
    if math == 'divides':
        e.insert(0, f_num / int(second_number))

#Initialize & define the buttons 

'''Number Buttons'''
button_1 = Button(root, text='1 ', padx=40, pady=20, command=lambda: button_click(1), fg='blue')
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2), fg='blue')
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3), fg='blue')
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4), fg='blue')
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5), fg='blue')
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6), fg='blue')
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7), fg='blue')
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8), fg='blue')
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9), fg='blue')
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0), fg='blue')

'''Operation Buttons'''
button_plus = Button(root, text='+', padx=39, pady=20, command=button_add)
button_minus = Button(root, text='-', padx=39, pady=20, command=button_minus)
button_multiply = Button(root, text='X', padx=39, pady=20, command=button_multiply)
button_divide = Button(root, text='%', padx=39, pady=20, command=button_divide)

'''Utility Buttons'''
button_equals = Button(root, text='=', padx=91, pady=20, command=equate)
button_clear = Button(root, text='c', padx=39, pady=20, command=button_clear, fg='red')
button_backspace = Button(root, text='<-', padx = 39, pady=20, command=button_backspace, fg='red')

#Button grid system

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_plus.grid(row=5, column=0)
button_minus.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_clear.grid(row=4, column=1)
button_equals.grid(row=5, column=1, columnspan=2)
button_backspace.grid(row=4, column=2, columnspan=2)

root.mainloop()