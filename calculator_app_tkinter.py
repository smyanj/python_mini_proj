import tkinter as tk

window=tk.Tk()
window.geometry("600x300")
window.title("Calculator App")

# creating the widgets
num1 = tk.Label(text = "Enter 1st Number: ")
num1.grid(column=0,row=0)
num1Entry = tk.Entry()
num1Entry.grid(column=1,row=0)

num2 = tk.Label(text = "Enter 2nd Number: ")
num2.grid(column=0,row=1)
num2Entry = tk.Entry()
num2Entry.grid(column=1,row=1)


opLabel = tk.Label(text = "Select the Operation: ")
opLabel.grid(column=0,row=2)

myOption = tk.StringVar(window)
myOption.set("Select")
opMenu = tk.OptionMenu(window, myOption, "Add","Subtract", "Multiply", "Divide")
opMenu.grid(column=1,row=2)

# button event method

def mathOperations():
    a=int(num1Entry.get())
    b=int(num2Entry.get())
    op=myOption.get()
    if(op=='Add'):
        s = a+b
        result = "The result is {0}".format(s)
    elif(op=='Subtract'):
        s = a-b
        result = "The result is {0}".format(s)
    elif(op=='Multiply'):
        s = a*b
        result = "The result is {0}".format(s)
    elif(op=='Divide'):
        s = a/b
        result = "The result is {0}".format(s)
    else:
        result = "Please select an operation"
    textArea = tk.Text(master=window,height=7,width=20)
    textArea.grid(column=1,row=3)
    textArea.insert(tk.END,result)

button=tk.Button(window,text="Calculate",command=mathOperations,bg="lightgreen")
button.grid(column=0,row=3)

window.mainloop()
