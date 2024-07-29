from tkinter import *
from collections import deque

root = Tk()
root.title("Styled Calculator")  # Optional: Set a title for the window

# Create a Text widget with improved styling
e = Text(root, width=35, height=4, borderwidth=5, relief=SUNKEN, font=("Arial", 16),state=DISABLED)

e.grid(row=0, column=0, columnspan=3, padx=15, pady=10, sticky="nsew")

# Define a function to update the Text widget
def button_click(val):
    e.config(state='normal')
    e.insert(END,val)
    e.config(state=DISABLED)
    return

def button_del():
    e.config(state='normal')
    s=len(e.get(1.0,END))-1
    if s > 1:  
        # Calculate the index of the last character
        s = f"1.0 + {s - 1}c"
    e.delete(s,END)
    e.config(state=DISABLED)
    
def button_clear():
    e.config(state='normal')
    e.delete(1.0,END)
    e.config(state=DISABLED)
    return

def button_equal():
    lst = deque()  # Initialize the deque
    e.config(state='normal')  # Make the Text widget editable
    
    # Retrieve the text from the Text widget, excluding the trailing newline
    s = e.get('1.0', END).strip()  # Remove leading/trailing whitespace
    
    a = ''  # Initialize an empty string for collecting operands
    
    # Parse the text
    for i in s:
        if i == '+':
            if a:
                lst.append(a)
                a = ''
            lst.append('add')
        elif i == '-':
            if a:
                lst.append(a)
                a = ''
            lst.append('sub')
        elif i == '*':
            if a:
                lst.append(a)
                a = ''
            lst.append('mul')
        elif i == '/':
            if a:
                lst.append(a)
                a = ''
            lst.append('div')
        elif i not in ' \n':  # Ignore spaces and newlines
            a += i
    
    # Append the last operand if any
    if a:
        lst.append(a)
    

    if(len(lst)==1):
        return
    # Evaluate the expression
    while len(lst) > 1:
        try:
            # Ensure there are enough elements to operate on
            if len(lst) < 3:
                e.delete(1.0,END)
                e.insert('1.0', 'Invalid Input!')
                e.config(state=DISABLED)
                return
            
            a = float(lst.popleft())
            op = lst.popleft()
            b = float(lst.popleft())
            
            if op == 'add':
                result = a + b
            elif op == 'sub':
                result = a - b
            elif op == 'mul':
                result = a * b
            elif op == 'div':
                if b != 0:
                    result = a / b
                else:
                    raise ZeroDivisionError("Division by zero")
            
            lst.appendleft(result)
        except (ValueError, ZeroDivisionError) as a:
            e.delete(1.0,END)
            e.insert('1.0', 'Invalid Input!')
            e.config(state=DISABLED)
            return
    
    # Display the result or an error message
    if len(lst) == 1:
        e.delete(1.0,END)
        e.insert('1.0', str(lst[0]))
    else:
        e.insert('1.0', 'Invalid Input!')
    
    e.config(state=DISABLED)  # Make the Text widget read-only again

# Create buttons with improved styling
button_style = {"padx": 20, "pady": 20, "font": ("Arial", 14), "bg": "#f0f0f0"}
#lambda function is used for the parameterized functions
button_1 = Button(root, text='1', **button_style, command=lambda : button_click('1'))
button_2 = Button(root, text='2', **button_style, command=lambda: button_click('2'))
button_3 = Button(root, text='3', **button_style, command=lambda: button_click('3'))
button_4 = Button(root, text='4', **button_style, command=lambda: button_click('4'))
button_5 = Button(root, text='5', **button_style, command=lambda: button_click('5'))
button_6 = Button(root, text='6', **button_style, command=lambda: button_click('6'))
button_7 = Button(root, text='7', **button_style, command=lambda: button_click('7'))
button_8 = Button(root, text='8', **button_style, command=lambda: button_click('8'))
button_9 = Button(root, text='9', **button_style, command=lambda: button_click('9'))
button_0 = Button(root, text='0', **button_style, command=lambda: button_click('0'))
button_p = Button(root, text='.', **button_style, command=lambda: button_click('.'))
button_del = Button(root, text='del', **button_style, command=button_del)
button_plus = Button(root, text='+', **button_style, command=lambda: button_click('+'))
button_minus = Button(root, text='-', **button_style, command=lambda: button_click('-'))
button_mult = Button(root, text='*', **button_style, command=lambda: button_click('*'))
button_div = Button(root, text='/', **button_style, command=lambda: button_click('/'))
button_clear = Button(root, text='clr', **button_style, command=button_clear)
button_eql = Button(root, text='=', **button_style, command=button_equal)
# Arrange buttons in a grid
#sticky='nsew': Makes the widget stretch to fill the entire cell, both horizontally and vertically.

button_1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
button_2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
button_3.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

button_4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
button_5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
button_6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

button_7.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
button_8.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
button_9.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

button_0.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
button_p.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
button_del.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

button_plus.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
button_minus.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
button_mult.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
button_div.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
button_clear.grid(row=6, column=1,padx=5, pady=5, sticky="nsew")
button_eql.grid(row=6, column=2,padx=5, pady=5, sticky="nsew")
# Configure grid to expand with window resizing


root.mainloop()
