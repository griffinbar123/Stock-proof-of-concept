# This is a proof of concept piece of code.
# Me and my friend are working on building a
# website using reacts and django (As of now)
# This is a simple app i made to give an example
# of one of the many functions we want our site to have.
# This is tkinter code that calls an alphavantage api
# to get info, and using matplotlib(among other things)
# it displays the data in a graph
# this is very basic(though i plan on making it better soon).
# To run a second company through, u have to close the window
# and restart. Like i said, i just made this as a POC for me
# and my friend

import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import gap

class Window(tk.Tk):
    # creates the window
    def __init__(self):
        tk.Tk.__init__(self)
        #creates text box
        self.entry = tk.Entry(self)
        #creates button
        self.button = tk.Button(self, text="Get", command=self.graph)
        self.button.pack()
        self.entry.pack()

    #graphs the data
    def graph(self):
        name = self.entry.get()
        self.close = gap.Gma()
        self.jclose = self.close.Aclose(name)
        self.entry = tk.Entry()
        self.figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax2 = self.figure2.add_subplot(111)
        self.line2 = FigureCanvasTkAgg(self.figure2,)
        self.line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        self.jclose.plot(kind='line', legend=True, ax=self.ax2, color='r', marker='o', fontsize=10)
        self.ax2.set_title('Months Vs. Adjusted Close Price for ' + name )

app = Window()
app.mainloop()