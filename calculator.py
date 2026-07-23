import tkinter as tk
button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "",] ]
right_symbols = ["/", "*", "-", "+" ,"="]
top_symbols = ["AC", "+/-", "%"]
row_count = len(button_values)
column_count = len(button_values[0])

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text="0",
                 font=("Arial", 45), 
                 background=color_black,
                 foreground=color_white,
                 anchor="e", 
                 width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="ew")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tk.Button(frame, text=value, font=("Arial", 30), 
                              width=column_count-1, height=1, 
                              command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.configure(background=color_black, foreground=color_light_gray)
        elif value in right_symbols:
            button.configure(background=color_orange, foreground=color_white)
        else:
            button.configure(background=color_light_gray, foreground=color_black)
        button.grid(row=row+1, column=column)  


frame.pack()

A = "0"       
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    B = None
    operator = None

def remove_zero_decimal(num):
    if num %1 == 0:
        num = int(num)
    return str(num) 

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "*":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "/": 
                    label["text"] = remove_zero_decimal(numA / numB) 

                clear_all()              
              
        elif value in "+-*/":
            if operator is None:
             A = label["text"]
             label["text"] = "0"
             B = "0" 
             operator = value  
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
           result = float(label["text"]) * -1
           label["text"] = remove_zero_decimal(result)

        elif value == "%": 
              result = float(label["text"]) / 100
              label["text"] = remove_zero_decimal(result)  

    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value

        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value

            else:
                label["text"] += value

window.mainloop()

