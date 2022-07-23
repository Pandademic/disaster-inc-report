# -*- coding: utf-8 -*-
import tkinter as tk

root = tk.Tk()
root.geometry("600x600")
root.title("Disaster inc. finance report")

months = ("January","Febuary","March","April","May","June","July","August","September","October","Novemeber","December")
profits = (70000,1234545,8000000,7817000,98753,12345,7891011,12131456,107623131,666666,101810101,16517151)

def findMax() -> (int,str):
    the_max = max(profits)
    month = months[profits.index(the_max)]
    return (the_max,month)

def findMin() -> (int,str):
    the_min = min(profits)
    month  = months[profits.index(the_min)]
    return (the_min,month)


maxLabel = tk.Label(root,text="Maximum Earnings in the form of (maximum,month) :")
minLabel = tk.Label(root,text="minimum Earnings in the form of (maximum,month) :")

maxLabel.pack()
minLabel.pack()

maxLabel["text"] += "\n"+str(findMax())
minLabel["text"] += "\n"+str(findMin())
root.mainloop()
