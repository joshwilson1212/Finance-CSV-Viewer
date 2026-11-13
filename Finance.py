import csv
import sys
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def openFile(file):
    fields = []
    rows = []
    with open(file,'r',encoding="utf8",errors='ignore') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return fields,rows

#a function that takes the date in and returns the week number of the year
def getMonth(row):

    month,day,year = (int(x) for x in row[0].split("/"))
    if day == 31:
        balance = int(row[3])
    return month,year,balance

def Main():
    
    try:
     file = sys.argv[1]
     fields, rows = openFile(file)
    except:
        print("Invalid Command Line Arguments: ")
        exit()
        
        
    MonthlyDifference = {}
    BalanceMonth = []
    MonthCompare = 0
    TransactionByMonth = {}
    
    for row in rows:
        Month,day,year = (int(x) for x in row[0].split("/"))

        #marks the balance of the account in the beginning of the months
        if MonthCompare != Month:
            balance = float((row[3][1:]).replace(',',''))
            BalanceMonth.append(balance)
        key = (f"{Month}-{str(year)[2:]}")
        value = float(row[2])
        
        #adds indivitaul transactiosn catigorized by months
        if key in TransactionByMonth:
            TransactionByMonth[key].append(value)
        else:
            TransactionByMonth.update({key:[value]})
        
        #totals up all transactions and spits out the final result catigoriezed by moth
        if key in MonthlyDifference:
            MonthlyDifference[key] = round(value + MonthlyDifference.get(key),2) 
        else:
            MonthlyDifference.update({key:value})
        MonthCompare = Month
    
    
    #reversing order of lists/dics to be in chronological order
    MonthlyDifference = dict(reversed(list(MonthlyDifference.items())))
    BalanceMonth = list(reversed(BalanceMonth))
    
    #setting up plot
    fig,ax = plt.subplots()
    
    #variables
    x = range(len(MonthlyDifference))
    #bar
    barx = ax.bar(x, list(MonthlyDifference.values()), align='center',label="Gross income")
    #ax.bar_label(barx,padding = 3)
    
    #line
    ax.plot(x,BalanceMonth,label="Account Balance")
    #for xy in zip(x,BalanceMonth):
    #    ax.annotate(BalanceMonth[xy[0]],xy=xy)
    
    #setting up x axis marks and zero line
    plt.xticks(x, list(MonthlyDifference.keys()))
    plt.axhline(y=0,color='r',linestyle='-')

    #marks y axis with a min of -600 and max of 10000 marking by 500 between the 2 min and max
    plt.yticks(np.arange(-6000,10000,500))
    
    #Labeling axis
    ax.set_xlabel("Month of the Year")
    ax.set_ylabel("Dollars")
    ax.set_title("Gross income against account balance")
    ax.legend(title="Legend",loc='upper left')

    ax.grid()
    
    fig.subplots_adjust(left=0.05, right=0.99, top=0.95, bottom=0.05)
    
    
    
    #starts up tkinter
    root = tk.Tk()
    root.title("embedded Matplotlib")
    
    #embeds the figure into a canvas that it then packed into a tkinter widget
    canvas = FigureCanvasTkAgg(fig,master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side="left",fill=tk.BOTH, expand=True)
    
    dropdown = ttk.Combobox(root, value = list(TransactionByMonth.keys())[::-1])
    dropdown.current(0)
    dropdown.pack(side="top")
    
    #lists the current transactions by month
    listbox = tk.Listbox(root,activestyle='none',height=60)
    listbox.pack(side="top",fill=tk.BOTH)
    
    
    def on_select(event):
        listbox.delete(0,tk.END)
        selected = dropdown.get()
        fill_listbox(selected)
    
    def fill_listbox(selected):
        for index,transactions in enumerate(TransactionByMonth[selected]):
            listbox.insert(tk.END,transactions)
            if transactions < 0:
                listbox.itemconfig(index,fg="red")
            else:
                listbox.itemconfig(index,fg="green")
                  
            
        
    dropdown.bind("<<ComboboxSelected>>",on_select)
    
    
    def quit_me():
        print("Quitting...")
        root.quit()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", quit_me)
    
    root.mainloop()


    
Main()
