from tkinter import *

def calculateInterest():
    principle = int(principleField.get())
    rate = float(rateField.get())
    time = int(timeField.get())
    
    cInterest = principle * pow((1 + rate/100), time)
    
    compoundField.insert(0, cInterest)
    
def clearCalc():
    principleField.delete(0, END)
    rateField.delete(0, END)
    timeField.delete(0, END)
    compoundField.delete(0, END)
    
    principleField.focus_set()
    
if __name__ == "__main__":
    root = Tk()
    
    root.configure(bg = 'light green')
    root.geometry("500x250")
    root.title("Compound Interest Calculator")
    
    lb1 = Label(root, text = 'Principle Amount :', fg = 'black', bg = 'red')
    lb2 = Label(root, text = 'Interest Rate (%) :', fg = 'black', bg = 'red')
    lb3 = Label(root, text = 'Time (Yrs) :', fg = 'black', bg = 'red')
    lb4 = Label(root, text = 'Compounded Amount :', fg = 'black', bg = 'red')
    
    lb1.grid(row = 1, column = 0, padx = 10, pady = 10)
    lb2.grid(row = 2, column = 0, padx = 10, pady = 10)
    lb3.grid(row = 3, column = 0, padx = 10, pady = 10)
    lb4.grid(row = 5, column = 0, padx = 10, pady = 10)
    
    principleField = Entry(root)
    rateField = Entry(root)
    timeField = Entry(root)
    compoundField = Entry(root)
    
    principleField.grid(row = 1, column = 1, padx = 10, pady = 10)
    rateField.grid(row = 2, column = 1, padx = 10, pady = 10)
    timeField.grid(row = 3, column = 1, padx = 10, pady = 10)
    compoundField.grid(row = 5, column = 1, padx = 10, pady = 10)
    
    button1 = Button(root, text = 'Submit', fg = 'black', bg = 'red', command = lambda: calculateInterest())
    button2 = Button(root, text = 'Clear', fg = 'black', bg = 'red', command = lambda: clearCalc())
    
    button1.grid(row = 4, column = 1)
    button2.grid(row = 6, column = 1)
    
    
    
    root.mainloop()