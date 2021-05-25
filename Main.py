#!/opt/local/bin/python

import tkinter as tk
import tkinter.ttk as ttk
import sys
from random import randint
import Eloïse

import threading

globstop = 0
mauvaisetage = False
portes_ouvertes = 0  # à 1 les portes sont complétement ouvertes, à 0 elles sont fermées
portes_bloquees = False
PORTES_UN_PEU_OUVERTES = 0.5  # à quelle proportion les portes s'ouvrent lorsqu'on clique sur le bouton associé
AUTORISATION_PORTES_OUVERTES = 0.0025  # on considère que les portes s'ouvrent sur 2m, on autorise une ouverture de 0.0025% de 2m qui font 5mm
bouge_portes_ouvertes = False


class MyTimer:
    global globstop

    def __init__(self, tempo, target, args=None, kwargs=None):
        if kwargs is None:
            kwargs = {}
        if args is None:
            args = []
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo

    def _run(self):
        if globstop:
            sys.exit()
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)

    def start(self):

        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()

    def stop(self):
        self._timer.cancel()


class Lift():
    global portes_ouvertes, portes_bloquees

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('ascenseur')

        self.CreerEtage()
        self.CreerElevator()
        self.CreerLouis()

        self.newWindow2 = tk.Toplevel(self.master)
        self.Eloise = Defaillance(self.newWindow2)

        self.buttonA = tk.Button(self.frame, text='Alarm')
        self.buttonA.pack()


        self.button5 = tk.Button(self.frame, text='5', command=self.Aller5)
        self.button5.pack()
        self.button4 = tk.Button(self.frame, text='4', command=self.Aller4)
        self.button4.pack()
        self.button3 = tk.Button(self.frame, text='3', command=self.Aller3)
        self.button3.pack()
        self.button2 = tk.Button(self.frame, text='2', command=self.Aller2)
        self.button2.pack()
        self.button1 = tk.Button(self.frame, text='1', command=self.Aller1)
        self.button1.pack()

        self.frame.pack()

        self.CurEtage = 1
        self.curMouvement = '0'
        self.target = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.CurPos = 0
        self.CurServed = 0
        self.CurTempo = 0
        self.UpdateColor()

    def Aller5(self):
        global portes_ouvertes, portes_bloquees
        if mauvaisetage:
            if self.CurPos < 10:
                if not portes_bloquees:
                    portes_ouvertes = 0
                    print("portes fermées")
                self.target[self.CurPos] = 4
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0
        else:
            if self.CurPos < 10:
                if not portes_bloquees:
                    portes_ouvertes = 0
                    print("portes fermées")
                self.target[self.CurPos] = 5
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0

    def Aller4(self):
        global portes_ouvertes, portes_bloquees
        if mauvaisetage:
            if self.CurPos < 10:
                if not portes_bloquees:
                    portes_ouvertes = 0
                    print("portes fermées")
                self.target[self.CurPos] = 3
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0
        else:
            if self.CurPos < 10:
                if not portes_bloquees:
                    portes_ouvertes = 0
                    print("portes fermées")
                self.target[self.CurPos] = 4
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0

    def Aller3(self):
        global portes_ouvertes, portes_bloquees
        if mauvaisetage:
            if self.CurPos < 10:
                if not portes_bloquees:
                    portes_ouvertes = 0
                    print("portes fermées")
                self.target[self.CurPos] = 2
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0
        else:
            if self.CurPos < 10:
                if not portes_bloquees:
                    portes_ouvertes = 0
                    print("portes fermées")
                self.target[self.CurPos] = 3
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0

    def Aller2(self):
        global portes_ouvertes, portes_bloquees
        if mauvaisetage:
            if self.CurPos < 10:
                if not portes_bloquees:
                    portes_ouvertes = 0
                    print("portes fermées")
                self.target[self.CurPos] = 1
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0
        else:
            if self.CurPos < 10:
                if not portes_bloquees:
                    portes_ouvertes = 0
                    print("portes fermées")
                self.target[self.CurPos] = 2
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0

    def Aller1(self):
        global portes_ouvertes, portes_bloquees
        if mauvaisetage:
            if self.CurPos < 10:
                if not portes_bloquees:
                    portes_ouvertes = 0
                    print("portes fermées")
                self.target[self.CurPos] = 5
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0
        else:
            if self.CurPos < 10:
                if not portes_bloquees:
                    portes_ouvertes = 0
                    print("portes fermées")
                self.target[self.CurPos] = 1
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0

    def CreerEtage(self):
        self.newWindow = tk.Toplevel(self.master)
        if mauvaisetage == True:
            self.Etages = Eloïse.Etages(self.newWindow, self)
        else:
            self.Etages = Etages(self.newWindow, self)

    def CreerElevator(self):

        self.newWindow = tk.Toplevel(self.master)
        self.Elevator = Elevator(self.newWindow)

    def CreerLouis(self):
        self.newWindow = tk.Toplevel(self.master)
        self.DefaillanceLouis = DefaillanceLouis(self.newWindow)

    def move(self):
        global portes_ouvertes, bouge_portes_ouvertes

        if portes_ouvertes >= AUTORISATION_PORTES_OUVERTES and bouge_portes_ouvertes == False:
            return
        # comment out for exam
        print(self.curMouvement)
        print(self.CurEtage)
        print(self.CurTempo)
        print(self.CurPos, self.CurServed)
        print(self.target)

        if self.CurEtage > 5:
            print("self.CurEtage > 5")
            self.CurEtage = 5
            self.curMouvement = '0'
        if self.CurEtage < 1:
            print("self.CurEtage < 1")
            self.CurEtage = 1
            self.curMouvement = '0'

        if self.curMouvement == '+' or self.curMouvement == '-' or self.curMouvement == 'pause':
            self.CurTempo = self.CurTempo + 1
        if self.CurTempo == 50 or self.CurTempo == 0:  # permet de donner une notion de temps entre les etages

            if self.curMouvement == 'pause':
                self.curMouvement = '0'

            if self.curMouvement == '+':
                self.CurEtage = self.CurEtage + 1
                if self.CurEtage == self.target[self.CurServed]:
                    self.curMouvement = 'pause'
                    self.target[self.CurServed] = 0
                    self.CurServed = self.CurServed + 1
                    if not portes_bloquees:
                        portes_ouvertes = 1
                        print("portes ouvertes")
                    if self.CurServed == 5:
                        self.CurServed = 0
                        self.target[self.CurPos] = randint(0, 5)
            if self.curMouvement == '-':
                self.CurEtage = self.CurEtage - 1
                if self.CurEtage == self.target[self.CurServed]:
                    self.curMouvement = 'pause'
                    self.target[self.CurServed] = 0
                    self.CurServed = self.CurServed + 1
                    if not portes_bloquees:
                        portes_ouvertes = 1
                        print("portes ouvertes")
                    if self.CurServed == 5:
                        self.CurServed = 0
                        self.target[self.CurServed] = randint(0, 5)

            self.UpdateColor()
            self.CurTempo = 0

        if self.curMouvement == '0':
            if self.target[self.CurServed] > 0:
                # print(self.CurServed)
                if self.CurEtage < self.target[self.CurServed]:
                    self.curMouvement = '+'
                    self.UpdateColor()
                if self.CurEtage > self.target[self.CurServed]:
                    self.curMouvement = '-'
                    self.UpdateColor()
                if self.target[self.CurServed] == self.CurEtage:
                    if self.CurServed == 9:
                        self.CurServed = 0
                    else:
                        self.CurServed = self.CurServed + 1
                        print(self.CurServed)

    def UpdateColor(self):
        #        print "UpdateColor", self.curMouvement, self.CurEtage
        if self.curMouvement == '0':
            if self.CurEtage == 1:
                self.Elevator.rouge1()
                self.Elevator.noir2()
                self.Elevator.noir3()
                self.Elevator.noir4()
                self.Elevator.noir5()
            elif self.CurEtage == 2:
                self.Elevator.noir1()
                self.Elevator.rouge2()
                self.Elevator.noir3()
                self.Elevator.noir4()
                self.Elevator.noir5()
            elif self.CurEtage == 3:
                self.Elevator.noir1()
                self.Elevator.noir2()
                self.Elevator.rouge3()
                self.Elevator.noir4()
                self.Elevator.noir5()
            elif self.CurEtage == 4:
                self.Elevator.noir1()
                self.Elevator.noir2()
                self.Elevator.noir3()
                self.Elevator.rouge4()
                self.Elevator.noir5()
            elif self.CurEtage == 5:
                self.Elevator.noir1()
                self.Elevator.noir2()
                self.Elevator.noir3()
                self.Elevator.noir4()
                self.Elevator.rouge5()

        elif self.curMouvement == 'pause':
            if self.CurEtage == 1:
                self.Elevator.vert1()
                self.Elevator.noir2()
                self.Elevator.noir3()
                self.Elevator.noir4()
                self.Elevator.noir5()
            elif self.CurEtage == 2:
                self.Elevator.noir1()
                self.Elevator.vert2()
                self.Elevator.noir3()
                self.Elevator.noir4()
                self.Elevator.noir5()
            elif self.CurEtage == 3:
                self.Elevator.noir1()
                self.Elevator.noir2()
                self.Elevator.vert3()
                self.Elevator.noir4()
                self.Elevator.noir5()
            elif self.CurEtage == 4:
                self.Elevator.noir1()
                self.Elevator.noir2()
                self.Elevator.noir3()
                self.Elevator.vert4()
                self.Elevator.noir5()
            elif self.CurEtage == 5:
                self.Elevator.noir1()
                self.Elevator.noir2()
                self.Elevator.noir3()
                self.Elevator.noir4()
                self.Elevator.vert5()


        elif self.curMouvement == '+':
            if self.CurEtage == 1:
                self.Elevator.orange1()
                self.Elevator.bleu2()
                self.Elevator.noir3()
                self.Elevator.noir4()
                self.Elevator.noir5()
            elif self.CurEtage == 2:
                self.Elevator.noir1()
                self.Elevator.orange2()
                self.Elevator.bleu3()
                self.Elevator.noir4()
                self.Elevator.noir5()
            elif self.CurEtage == 3:
                self.Elevator.noir1()
                self.Elevator.noir2()
                self.Elevator.orange3()
                self.Elevator.bleu4()
                self.Elevator.noir5()
            elif self.CurEtage == 4:
                self.Elevator.noir1()
                self.Elevator.noir2()
                self.Elevator.noir3()
                self.Elevator.orange4()
                self.Elevator.bleu5()


        elif self.curMouvement == '-':
            if self.CurEtage == 2:
                self.Elevator.bleu1()
                self.Elevator.orange2()
                self.Elevator.noir3()
                self.Elevator.noir4()
                self.Elevator.noir5()
            elif self.CurEtage == 3:
                self.Elevator.noir1()
                self.Elevator.bleu2()
                self.Elevator.orange3()
                self.Elevator.noir4()
                self.Elevator.noir5()
            elif self.CurEtage == 4:
                self.Elevator.noir1()
                self.Elevator.noir2()
                self.Elevator.bleu3()
                self.Elevator.orange4()
                self.Elevator.noir5()
            elif self.CurEtage == 5:
                self.Elevator.noir1()
                self.Elevator.noir2()
                self.Elevator.noir3()
                self.Elevator.bleu4()
                self.Elevator.orange5()

    def sortir(self):
        global globstop
        globstop = 1
        sys.exit(1)


class Etages(Lift):
    def __init__(self, master, Lift):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('Etages')

        self.button5u = tk.Button(self.frame, text='5 ^', command=Lift.Aller5)
        self.button5u.pack()
        self.button5d = tk.Button(self.frame, text='5 v', command=Lift.Aller5)
        self.button5d.pack()

        self.button4u = tk.Button(self.frame, text='4 ^', command=Lift.Aller4)
        self.button4u.pack()
        self.button4d = tk.Button(self.frame, text='4 v', command=Lift.Aller4)
        self.button4d.pack()

        self.button3u = tk.Button(self.frame, text='3 ^', command=Lift.Aller3)
        self.button3u.pack()
        self.button3d = tk.Button(self.frame, text='3 v', command=Lift.Aller3)
        self.button3d.pack()

        self.button2u = tk.Button(self.frame, text='2 ^', command=Lift.Aller2)
        self.button2u.pack()
        self.button2d = tk.Button(self.frame, text='2 v', command=Lift.Aller2)
        self.button2d.pack()

        self.button1u = tk.Button(self.frame, text='1 ^', command=Lift.Aller1)
        self.button1u.pack()
        self.button1d = tk.Button(self.frame, text='1 v', command=Lift.Aller1)
        self.button1d.pack()

        self.master.geometry("+200+200")

        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


class Elevator:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('Position')

        style = ttk.Style()
        style.configure("TButton", padding=(0, 5, 0, 5))

        style.configure("Red.TButton", foreground='red')
        style.configure("Blue.TButton", foreground='blue')
        style.configure("Green.TButton", foreground='green')
        style.configure("Orange.TButton", foreground='orange')
        style.configure("Black.Tbutton", foreground='black')

        self.button5 = ttk.Button(self.frame, text='#_5_#')
        self.button5.configure(style="Red.TButton")
        self.button5.pack()

        self.button4 = ttk.Button(self.frame, text='#_4_#')
        self.button4.configure(style="Blue.TButton")
        self.button4.pack()

        self.button3 = ttk.Button(self.frame, text='#_3_#')
        self.button3.configure(style="Green.TButton")
        self.button3.pack()

        self.button2 = ttk.Button(self.frame, text='#_2_#')
        self.button2.pack()
        self.button2.configure(style="Orange.TButton")

        self.button1 = ttk.Button(self.frame, text='#_1_#')
        self.button1.configure(style="Black.TButton")
        self.button1.pack()

        self.master.geometry("+400+200")

        self.frame.pack()

    def rouge5(self):
        self.button5.configure(style="Red.TButton")
        self.button5.pack()

    def bleu5(self):
        self.button5.configure(style="Blue.TButton")
        self.button5.pack()

    def vert5(self):
        self.button5.configure(style="Green.TButton")
        self.button5.pack()

    def orange5(self):
        self.button5.configure(style="Orange.TButton")
        self.button5.pack()

    def noir5(self):
        self.button5.configure(style="Black.TButton")
        self.button5.pack()

    def rouge4(self):
        self.button4.configure(style="Red.TButton")
        self.button4.pack()

    def bleu4(self):
        self.button4.configure(style="Blue.TButton")
        self.button4.pack()

    def vert4(self):
        self.button4.configure(style="Green.TButton")
        self.button4.pack()

    def orange4(self):
        self.button4.configure(style="Orange.TButton")
        self.button4.pack()

    def noir4(self):
        self.button4.configure(style="Black.TButton")
        self.button4.pack()

    def rouge3(self):
        self.button3.configure(style="Red.TButton")
        self.button3.pack()

    def bleu3(self):
        self.button3.configure(style="Blue.TButton")
        self.button3.pack()

    def vert3(self):
        self.button3.configure(style="Green.TButton")
        self.button3.pack()

    def orange3(self):
        self.button3.configure(style="Orange.TButton")
        self.button3.pack()

    def noir3(self):
        self.button3.configure(style="Black.TButton")
        self.button3.pack()

    def rouge2(self):
        self.button2.configure(style="Red.TButton")
        self.button2.pack()

    def bleu2(self):
        self.button2.configure(style="Blue.TButton")
        self.button2.pack()

    def vert2(self):
        self.button2.configure(style="Green.TButton")
        self.button2.pack()

    def orange2(self):
        self.button2.configure(style="Orange.TButton")
        self.button2.pack()

    def noir2(self):
        self.button2.configure(style="Black.TButton")
        self.button2.pack()

    def rouge1(self):
        self.button1.configure(style="Red.TButton")
        self.button1.pack()

    def bleu1(self):
        self.button1.configure(style="Blue.TButton")
        self.button1.pack()

    def vert1(self):
        self.button1.configure(style="Green.TButton")
        self.button1.pack()

    def orange1(self):
        self.button1.configure(style="Orange.TButton")
        self.button1.pack()

    def noir1(self):
        self.button1.configure(style="Black.TButton")
        self.button1.pack()


class DefaillanceLouis:

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
        self.button5 = tk.Button(self.frame, text='debloquer les portes manuellement', command=self.debloquerPortes)
        self.button5.pack()
        self.button6 = tk.Button(self.frame, text='l\'ascenceur bouge avec les portes ouvertes',
                                 command=self.bougePortesOuvertes)
        self.button6.pack()

        self.frame.pack()

    def fPortes(self):
        global portes_ouvertes
        portes_ouvertes = 0
        print("portes fermées")

    def ouvPortes(self):
        global portes_ouvertes
        portes_ouvertes = 1
        print("portes ouvertes")

    def ouvUnPeuPortes(self):
        global portes_ouvertes, PORTES_UN_PEU_OUVERTES
        portes_ouvertes = PORTES_UN_PEU_OUVERTES
        print("portes ouvertes à " + str(PORTES_UN_PEU_OUVERTES * 100) + "%")

    def bloquerPortes(self):
        global portes_bloquees
        portes_bloquees = True

    def debloquerPortes(self):
        global portes_bloquees
        portes_bloquees = False

    def bougePortesOuvertes(self):
        global bouge_portes_ouvertes
        bouge_portes_ouvertes = True

class Defaillance:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('Defaillances Eloïse')

        self.button2 = tk.Button(self.frame, text='2e defaillance: mauvais étage', command=self.def2)
        self.button2.pack()

        self.frame.pack()

    def def2(self):
        global mauvaisetage
        mauvaisetage = True

def main():
    root = tk.Tk()
    app = Lift(root)
    root.protocol("WM_DELETE_WINDOW", app.sortir)
    Cron = MyTimer(0.02, app.move)
    Cron.start()
    root.mainloop()


if __name__ == '__main__':
    main()
