from tkinter import *

class LoanCalculator:
    
    def __init__(self):
        
        win = Tk()
        win.title("Loan Calculator")
        
        Label(win, text = "Annual Interest Rate").grid(row = 1, column = 1, sticky = W)
        Label(win, text = "Number of Years").grid(row = 2, column = 1, sticky = W)
        Label(win, text = "Loan Amount").grid(row = 3, column = 1, sticky = W)
        Label(win, text = "Monthly Payment").grid(row = 4, column = 1, sticky = W)
        Label(win, text = "Total Payment").grid(row = 5, column = 1, sticky = W)
        
        self.annualInterestRateVar = StringVar()
        Entry(win, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2)
        
        self.numberOfYearsVar = StringVar()
        Entry(win, textvariable= self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2)
        
        self.loanAmountVar = StringVar()
        Entry(win, textvariable= self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)
        
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(win, textvariable= self.monthlyPaymentVar, justify = RIGHT).grid(row = 4, column = 2, sticky = E)
        
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(win, textvariable= self.totalPaymentVar).grid(row = 5, column = 2, sticky = E)
        
        btComputePayment = Button(win, text = "Compute Payment", command = self.computePayment).grid(row = 6, column = 2, sticky = E)
        
        win.mainloop()
        
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get()))
        
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
        
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))
        
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        #compute monthly payment
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment
        
if __name__ == "__main__":
    LoanCalculator()
    exit(0)
        
        
        