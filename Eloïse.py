#!/opt/local/bin/python

import tkinter as tk
import Main
import tkinter.ttk as ttk
import time
import sys
from random import randint

import threading

class Defaillance:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('Defaillances Eloïse')

        self.button2 = tk.Button(self.frame, text='2e defaillance: mauvais étage', command=self.def2)
        self.button2.pack()

        self.frame.pack()

    def def2(self):
        Main.mauvaisetage = True

""""
    class Etages(Main.Lift):
        def __init__(self, master, Lift):
            self.master = master
            self.frame = tk.Frame(self.master)

            self.master.title('Etages')

            self.button5u = tk.Button(self.frame, text='5 ^', command=Lift.Aller1)
            self.button5u.pack()
            self.button5d = tk.Button(self.frame, text='5 v', command=Lift.Aller4)
            self.button5d.pack()

            self.button4u = tk.Button(self.frame, text='4 ^', command=Lift.Aller5)
            self.button4u.pack()
            self.button4d = tk.Button(self.frame, text='4 v', command=Lift.Aller3)
            self.button4d.pack()

            self.button3u = tk.Button(self.frame, text='3 ^', command=Lift.Aller4)
            self.button3u.pack()
            self.button3d = tk.Button(self.frame, text='3 v', command=Lift.Aller2)
            self.button3d.pack()

            self.button2u = tk.Button(self.frame, text='2 ^', command=Lift.Aller3)
            self.button2u.pack()
            self.button2d = tk.Button(self.frame, text='2 v', command=Lift.Aller1)
            self.button2d.pack()

            self.button1u = tk.Button(self.frame, text='1 ^', command=Lift.Aller2)
            self.button1u.pack()
            self.button1d = tk.Button(self.frame, text='1 v', command=Lift.Aller5)
            self.button1d.pack()

            self.master.geometry("+200+200")

            self.frame.pack()

        def close_windows(self):
            self.master.destroy()
"""
