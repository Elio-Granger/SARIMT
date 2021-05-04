import tkinter as tk

class Defaillance:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('Defaillances Louis')

        self.button1 = tk.Button(self.frame, text='1ere defaillance', command=Defaillance.def1)
        self.button1.pack()

        self.frame.pack()

    def def1(self):
        a=0

