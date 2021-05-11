import tkinter as tk
import Main

class Defaillance:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('Defaillances Louis')

        self.button1 = tk.Button(self.frame, text='fermer les portes manuellement', command=self.fPortes)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text='ouvrir les portes manuellement', command=self.ouvPortes)
        self.button2.pack()
        self.button3 = tk.Button(self.frame, text='ouvrir un peu les portes manuellement', command=self.ouvUnPeuPortes)
        self.button3.pack()
        self.button4 = tk.Button(self.frame, text='bloquer les portes', command=self.bloquerPortes)
        self.button4.pack()
        self.button5 = tk.Button(self.frame, text='debloquer les portes manuellement',
                                 command=self.debloquerPortes)
        self.button5.pack()

        self.frame.pack()

    def fPortes(self):
        Main.portes_ouvertes=0

    def ouvPortes(self):
        Main.portes_ouvertes=1

    def ouvUnPeuPortes(self):
        Main.portes_ouvertes = Main.PORTES_UN_PEU_OUVERTES

    def bloquerPortes(self):
        Main.portes_bloquees=True


    def debloquerPortes(self):
        Main.portes_bloquees=False

