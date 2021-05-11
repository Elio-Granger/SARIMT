import tkinter as tk
import Main

class Defaillance:
    portes_ouvertes = 0
    portes_bloquees = False
    PORTES_UN_PEU_OUVERTES = 0.5  # à 1 les portes sont complétement ouvertes, à 0 elles sont fermées
    AUTORISATION_PORTES_OUVERTES = 0.0025  #on considère que les portes s'ouvrent sur 2m, on autorise une ouverture de 0.0025% de 2m qui font 5mm

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
        self.button5 = tk.Button(self.frame, text='debloquer les portes manuellement',command=self.debloquerPortes)
        self.button5.pack()

        self.frame.pack()

    def fPortes(self):
        global portes_ouvertes
        portes_ouvertes=0

    def ouvPortes(self):
        global portes_ouvertes
        portes_ouvertes=1

    def ouvUnPeuPortes(self):
        global portes_ouvertes, PORTES_UN_PEU_OUVERTES
        portes_ouvertes = PORTES_UN_PEU_OUVERTES

    def bloquerPortes(self):
        global portes_bloquees
        portes_bloquees=True


    def debloquerPortes(self):
        global portes_bloquees
        portes_bloquees=False

