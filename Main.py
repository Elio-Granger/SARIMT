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
mauvaisePorte = False
curMouvement='0'

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

class descente_impossible():
    def __init__(self):
        self.activation = "disable"

    def activate(self):
        self.activation = "enable"

    def desactivate(self):
        self.activation = "disable"

    def status(self):
        return self.activation


class defaillance(descente_impossible):
    def __init__(self, master, descente_impossible):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry('200x200')
        self.master.title('Défaillance')
        self.buttonDesactivation = tk.Button(self.frame, text='Désactiver descente',command=descente_impossible.activate)
        self.buttonDesactivation.pack()
        self.buttonActivation = tk.Button(self.frame, text='Activer descente',command=descente_impossible.desactivate)
        self.buttonActivation.pack()
        self.frame.pack()

descente_impossible = descente_impossible()


class Lift():
    global portes_ouvertes, portes_bloquees, curMouvement
    global descente_impossible

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry('200x200')
        self.master.title('ascenseur')

        self.CreerEtage()
        self.CreerElevator()
        self.CreerLouis()
        self.CreerPortes()
        self.CreerDefaillance()

        self.newWindow2 = tk.Toplevel(self.master)
        self.Eloise = DefaillanceElo(self.newWindow2)

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

        self.CurEtage = 5
        curMouvement = '0'
        self.target = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.CurPos = 0
        self.CurServed = 0
        self.CurTempo = 0
        self.UpdateColor()

    def Aller5(self):
        if mauvaisetage:
            if self.CurPos < 10:
                self.target[self.CurPos] = 4
                self.ordrePriorite()
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0
        if descente_impossible.status() == "enable":
            if self.CurEtage > self.target[self.CurPos]:
                if self.CurPos < 10:
                    self.target[self.CurPos] = 5
                if self.CurPos == 10:
                    self.CurPos = 0
            else:
                if self.CurPos < 10:
                    self.target[self.CurPos] = 5
                    self.ordrePriorite()
                    self.CurPos = self.CurPos + 1
                    if self.CurPos == 10:
                        self.CurPos = 0
        else:
            if self.CurPos < 10:
                self.target[self.CurPos] = 5
                self.ordrePriorite()
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0

    def Aller4(self):
        if mauvaisetage:
            if self.CurPos < 10:
                self.target[self.CurPos] = 3
                self.ordrePriorite()
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0
        if descente_impossible.status() == "enable":
            if self.CurEtage > self.target[self.CurPos]:
                if self.CurPos < 10:
                    self.target[self.CurPos] = 4
                if self.CurPos == 10:
                    self.CurPos = 0
            else:
                if self.CurPos < 10:
                    self.target[self.CurPos] = 4
                    self.ordrePriorite()
                    self.CurPos = self.CurPos + 1
                    if self.CurPos == 10:
                        self.CurPos = 0
        else:
            if self.CurPos < 10:
                self.target[self.CurPos] = 4
                self.ordrePriorite()
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0

    def Aller3(self):
        if mauvaisetage:
            if self.CurPos < 10:
                self.target[self.CurPos] = 2
                self.ordrePriorite()
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0
        if descente_impossible.status() == "enable":
            if self.CurEtage > self.target[self.CurPos]:
                if self.CurPos < 10:
                    self.target[self.CurPos] = 3
                if self.CurPos == 10:
                    self.CurPos = 0
            else:
                if self.CurPos < 10:
                    self.target[self.CurPos] = 3
                    self.ordrePriorite()
                    self.CurPos = self.CurPos + 1
                    if self.CurPos == 10:
                        self.CurPos = 0
        else:
            if self.CurPos < 10:
                self.target[self.CurPos] = 3
                self.ordrePriorite()
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0

    def Aller2(self):
        if mauvaisetage:
            if self.CurPos < 10:
                self.target[self.CurPos] = 1
                self.ordrePriorite()
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0
        if descente_impossible.status() == "enable":
            if self.CurEtage > self.target[self.CurPos]:
                if self.CurPos < 10:
                    self.target[self.CurPos] = 2
                if self.CurPos == 10:
                    self.CurPos = 0
            else:
                if self.CurPos < 10:
                    self.target[self.CurPos] = 2
                    self.ordrePriorite()
                    self.CurPos = self.CurPos + 1
                    if self.CurPos == 10:
                        self.CurPos = 0
        else:
            if self.CurPos < 10:
                self.target[self.CurPos] = 2
                self.ordrePriorite()
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0

    def Aller1(self):
        if mauvaisetage:
            if self.CurPos < 10:
                self.target[self.CurPos] = 5
                self.ordrePriorite()
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0
        if descente_impossible.status() == "enable":
            if self.CurEtage > self.target[self.CurPos]:
                if self.CurPos < 10:
                    self.target[self.CurPos] = 1
                if self.CurPos == 10:
                    self.CurPos = 0
            else:
                if self.CurPos < 10:
                    self.target[self.CurPos] = 1
                    self.ordrePriorite()
                    self.CurPos = self.CurPos + 1
                    if self.CurPos == 10:
                        self.CurPos = 0
        else:
            if self.CurPos < 10:
                self.target[self.CurPos] = 1
                self.ordrePriorite()
                self.CurPos = self.CurPos + 1
                if self.CurPos == 10:
                    self.CurPos = 0


    def ordrePriorite(self):

        if self.target[(self.CurServed + 1) % 10] in range(min(self.CurEtage, self.target[self.CurServed]), max(self.CurEtage, self.target[self.CurServed])):
            self.target[(self.CurServed + 1) % 10], self.target[self.CurServed] = self.target[self.CurServed], self.target[(self.CurServed + 1) % 10]

        i=self.CurServed
        while(i!=self.CurPos):
            if self.target[(i + 2) % 10] in range(min(self.target[i], self.target[(i + 1) % 10]),max(self.target[i], self.target[(i + 1) % 10])):
                self.target[(i + 2) % 10], self.target[(i + 1) % 10] = self.target[(i + 1) % 10], self.target[(i + 2) % 10]
            i = (i + 1) % 10



    def CreerEtage(self):
        self.newWindow = tk.Toplevel(self.master)
        if mauvaisetage == True:
            self.Etages = Eloïse.Etages(self.newWindow, self)
        else:
            self.Etages = Etages(self.newWindow, self)

    def CreerPortes(self):
        self.newWindow = tk.Toplevel(self.master)
        self.Etages = Double_porte_Elio(self.newWindow)

    def CreerElevator(self):

        self.newWindow = tk.Toplevel(self.master)
        self.Elevator = Elevator(self.newWindow)

    def CreerLouis(self):
        self.newWindow = tk.Toplevel(self.master)
        self.DefaillanceLouis = DefaillanceLouis(self.newWindow,self.Elevator)

    def CreerDefaillance(self):
        self.newWindow = tk.Toplevel(self.master)
        self.defaillance = defaillance(self.newWindow, descente_impossible)

    def move(self):
        global portes_ouvertes, bouge_portes_ouvertes, curMouvement

        self.UpdateColor()

        # comment out for exam
        #print("curMouvement "+curMouvement)
        #print("curEtage ",self.CurEtage)
        #print("CurTempo"+self.CurTempo)
        #print("CurPos: ",self.CurPos,"  /  CurServed: ", self.CurServed)
        #print("target ",self.target)

        if self.CurEtage > 5:
            self.CurEtage = 5
            curMouvement = '0'
        if self.CurEtage < 1:
            self.CurEtage = 1
            curMouvement = '0'

      #  if curMouvement == '+' or curMouvement == '-' or curMouvement == 'p':

        self.CurTempo = self.CurTempo + 1

        if self.CurTempo == 50 or self.CurTempo == 0:  # permet de donner une notion de temps entre les etages

            #print("curMouvement " + curMouvement)
            #print("curEtage ", self.CurEtage)
            # print("CurTempo"+self.CurTempo)
            #print("CurPos: ", self.CurPos, "  /  CurServed: ", self.CurServed)
            #print("target ", self.target)

            if curMouvement == 'p':
                curMouvement = '0'

            if curMouvement == '0':
                if self.target[self.CurServed] > 0:
                    if self.CurEtage < self.target[self.CurServed]:
                        curMouvement = '+'
                        self.UpdateColor()
                    if self.CurEtage > self.target[self.CurServed]:
                        curMouvement = '-'
                        self.UpdateColor()
                    if self.target[self.CurServed] == self.CurEtage:
                        if self.CurServed == 10:
                            self.CurServed = 0
                        else:
                            self.CurServed = self.CurServed + 1


            if portes_ouvertes < AUTORISATION_PORTES_OUVERTES or bouge_portes_ouvertes == True:
                if curMouvement == '+':
                    self.CurEtage = self.CurEtage + 1
                    if self.CurEtage == self.target[self.CurServed]:
                        curMouvement = 'p'
                        self.target[self.CurServed] = 0
                        self.CurServed = self.CurServed + 1
                        if self.CurServed == 10:
                            self.CurServed = 0
                            # self.target[self.CurPos] = randint(0, 5)   #pas compris cette ligne
                # if descente_impossible.status() == "enable":
                #     self.curMouvement = '0'
                # else:
                if curMouvement == '-':
                    self.CurEtage = self.CurEtage - 1
                    if self.CurEtage == self.target[self.CurServed]:
                        curMouvement = 'p'
                        self.target[self.CurServed] = 0
                        self.CurServed = self.CurServed + 1
                        if self.CurServed == 10:
                            self.CurServed = 0
                                # self.target[self.CurServed] = randint(0, 5)    #pas compris cette ligne

            self.UpdateColor()
            self.CurTempo = 0


    def UpdateColor(self):
        global portes_ouvertes, portes_bloquees,curEtage
        curEtage=self.CurEtage
        #        print "UpdateColor", curMouvement, self.CurEtage
        self.Elevator.check_Changes()
        if curMouvement == '0':
            if portes_bloquees==False:
                portes_ouvertes=0
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

            statut = portes[self.CurEtage - 1]
            if mauvaisePorte == True:
                if statut == 0:
                    statut = 1
                else:
                    statut = 0
            self.Elevator.Door_To_Red(self.CurEtage, portes[statut])

        elif curMouvement == 'p':
            if portes_bloquees==False:
                portes_ouvertes=1
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

            statut = portes[self.CurEtage - 1]
            if mauvaisePorte == True:
                if statut == 0:
                    statut = 1
                else:
                    statut = 0
            self.Elevator.Door_To_Green(self.CurEtage, statut)


        elif curMouvement == '+':
            if portes_bloquees==False:
                portes_ouvertes=0
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

           # print(self.CurEtage)
            statut = portes[self.CurEtage - 1]
            if mauvaisePorte == True:
                if statut == 0:
                    statut = 1
                else:
                    statut = 0
            self.Elevator.Door_To_Red(self.CurEtage, statut)


        elif curMouvement == '-':
            if portes_bloquees==False:
                portes_ouvertes=0
            if self.CurEtage == 2:
                if descente_impossible.status() == "enable":
                    self.Elevator.noir1()
                    self.Elevator.rouge2()
                    self.Elevator.noir3()
                    self.Elevator.noir4()
                    self.Elevator.noir5()
                else:
                    self.Elevator.bleu1()
                    self.Elevator.orange2()
                    self.Elevator.noir3()
                    self.Elevator.noir4()
                    self.Elevator.noir5()
            if self.CurEtage == 3:
                if descente_impossible.status() == "enable":
                    self.Elevator.noir1()
                    self.Elevator.noir2()
                    self.Elevator.rouge3()
                    self.Elevator.noir4()
                    self.Elevator.noir5()
                else:
                    self.Elevator.noir1()
                    self.Elevator.bleu2()
                    self.Elevator.orange3()
                    self.Elevator.noir4()
                    self.Elevator.noir5()
            if self.CurEtage == 4:
                if descente_impossible.status() == "enable":
                    self.Elevator.noir1()
                    self.Elevator.noir2()
                    self.Elevator.noir3()
                    self.Elevator.rouge4()
                    self.Elevator.noir5()
                else:
                    self.Elevator.noir1()
                    self.Elevator.noir2()
                    self.Elevator.bleu3()
                    self.Elevator.orange4()
                    self.Elevator.noir5()
            if self.CurEtage == 5:
                if descente_impossible.status() == "enable":
                    self.Elevator.noir1()
                    self.Elevator.noir2()
                    self.Elevator.noir3()
                    self.Elevator.noir4()
                    self.Elevator.rouge5()
                else:
                    self.Elevator.noir1()
                    self.Elevator.noir2()
                    self.Elevator.noir3()
                    self.Elevator.bleu4()
                    self.Elevator.orange5()

            statut = portes[self.CurEtage - 1]
            if mauvaisePorte == True:
                if statut == 0:
                    statut = 1
                else:
                    statut = 0
            self.Elevator.Door_To_Red(self.CurEtage, statut)

    def sortir(self):
        global globstop
        globstop = 1
        sys.exit(1)


class Etages(Lift):
    def __init__(self, master, Lift):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry('200x200')
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
        self.master.geometry('200x200')
        self.master.title('Position')

        style = ttk.Style()
        style.configure("TButton", padding=(0, 5, 0, 5))

        style.configure("Red.TButton", foreground='red')
        style.configure("Blue.TButton", foreground='blue')
        style.configure("Green.TButton", foreground='green')
        style.configure("Orange.TButton", foreground='orange')
        style.configure("Black.Tbutton", foreground='black')

        # ----------------------(Buttons 5)---------------------- #
        self.frame5 = tk.Frame(self.frame)

        self.button5 = ttk.Button(self.frame5, text='#_5_#')
        self.button5_back = ttk.Button(self.frame5, text='B5')
        self.button5_front = ttk.Button(self.frame5, text='F5')

        self.button5_back.pack(side=tk.LEFT)
        self.button5_front.pack(side=tk.RIGHT)
        self.button5.pack(side=tk.RIGHT)

        self.button5.configure(style="Red.TButton")

        self.frame5.pack(expand=True)
        # ----------------------(Buttons 4)---------------------- #

        self.frame4 = tk.Frame(self.frame)

        self.button4 = ttk.Button(self.frame4, text='#_4_#')
        self.button4_back = ttk.Button(self.frame4, text='B4')
        self.button4_front = ttk.Button(self.frame4, text='F4')

        self.button4_back.pack(side=tk.LEFT)
        self.button4_front.pack(side=tk.RIGHT)
        self.button4.pack(side=tk.RIGHT)

        self.button4.configure(style="Blue.TButton")

        self.frame4.pack(expand=True)
        # ----------------------(Buttons 3)---------------------- #

        self.frame3 = tk.Frame(self.frame)

        self.button3 = ttk.Button(self.frame3, text='#_3_#')
        self.button3_back = ttk.Button(self.frame3, text='B3')
        self.button3_front = ttk.Button(self.frame3, text='F3')

        self.button3_back.pack(side=tk.LEFT)
        self.button3_front.pack(side=tk.RIGHT)
        self.button3.pack(side=tk.RIGHT)

        self.button3.configure(style="Green.TButton")

        self.frame3.pack(expand=True)
        # ----------------------(Buttons 2)---------------------- #

        self.frame2 = tk.Frame(self.frame)

        self.button2 = ttk.Button(self.frame2, text='#_2_#')
        self.button2_back = ttk.Button(self.frame2, text='B2')
        self.button2_front = ttk.Button(self.frame2, text='F2')

        self.button2_back.pack(side=tk.LEFT)
        self.button2_front.pack(side=tk.RIGHT)
        self.button2.pack(side=tk.RIGHT)

        self.button2.configure(style="Orange.TButton")

        self.frame2.pack(expand=True)
        # ----------------------(Buttons 1)---------------------- #
        self.frame1 = tk.Frame(self.frame)

        self.button1 = ttk.Button(self.frame1, text='#_1_#')
        self.button1_back = ttk.Button(self.frame1, text='B1')
        self.button1_front = ttk.Button(self.frame1, text='F1')

        self.button1.configure(style="Black.TButton")

        self.button1_back.pack(side=tk.LEFT)
        self.button1_front.pack(side=tk.RIGHT)
        self.button1.pack(side=tk.RIGHT)

        self.frame1.pack(expand=True)

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


    def Door_To_Green(self,etage,statut):
        if statut == 0 :
            if etage == 1:
                self.button1_back.configure(style="chosen.TButton")
            elif etage == 2 :
                self.button2_back.configure(style="chosen.TButton")
            elif etage == 3 :
                self.button3_back.configure(style="chosen.TButton")
            elif etage == 3 :
                self.button3_back.configure(style="chosen.TButton")
            elif etage == 4 :
                self.button4_back.configure(style="chosen.TButton")
            elif etage == 5 :
                self.button5_back.configure(style="chosen.TButton")

        elif statut == 1 :
            if etage == 1:
                self.button1_front.configure(style="chosen.TButton")
            elif etage == 2 :
                self.button2_front.configure(style="chosen.TButton")
            elif etage == 3 :
                self.button3_front.configure(style="chosen.TButton")
            elif etage == 3 :
                self.button3_front.configure(style="chosen.TButton")
            elif etage == 4 :
                self.button4_front.configure(style="chosen.TButton")
            elif etage == 5 :
                self.button5_front.configure(style="chosen.TButton")

    def Door_To_Red(self,etage,statut):
        if statut == 0 :
            if etage == 1:
                self.button1_back.configure(style="unchosen.TButton")
            elif etage == 2 :
                self.button2_back.configure(style="unchosen.TButton")
            elif etage == 3 :
                self.button3_back.configure(style="unchosen.TButton")
            elif etage == 3 :
                self.button3_back.configure(style="unchosen.TButton")
            elif etage == 4 :
                self.button4_back.configure(style="unchosen.TButton")
            elif etage == 5 :
                self.button5_back.configure(style="unchosen.TButton")

        elif statut == 1 :
            if etage == 1:
                self.button1_front.configure(style="unchosen.TButton")
            elif etage == 2 :
                self.button2_front.configure(style="unchosen.TButton")
            elif etage == 3 :
                self.button3_front.configure(style="unchosen.TButton")
            elif etage == 3 :
                self.button3_front.configure(style="unchosen.TButton")
            elif etage == 4 :
                self.button4_front.configure(style="unchosen.TButton")
            elif etage == 5 :
                self.button5_front.configure(style="unchosen.TButton")

    def check_Changes(self):
        for i in range (5):
            if i==0 :
                if (self.button1_back.configure().get('style').__contains__("unchosen.TButton")) and self.button1_front.configure().get('style').__contains__("unchosen.TButton"):
                    self.button1_back.configure(style="blank.TButton")
                    self.button1_front.configure(style="blank.TButton")
                elif (self.button1_back.configure().get('style').__contains__("chosen.TButton")) and self.button1_front.configure().get('style').__contains__("chosen.TButton"):
                    self.button1_back.configure(style="blank.TButton")
                    self.button1_front.configure(style="blank.TButton")
            elif i==1 :
                if (self.button2_back.configure().get('style').__contains__("unchosen.TButton")) and self.button2_front.configure().get('style').__contains__("unchosen.TButton"):
                    self.button2_back.configure(style="blank.TButton")
                    self.button2_front.configure(style="blank.TButton")
                elif (self.button2_back.configure().get('style').__contains__("chosen.TButton")) and self.button2_front.configure().get('style').__contains__("chosen.TButton"):
                    self.button2_back.configure(style="blank.TButton")
                    self.button2_front.configure(style="blank.TButton")
            elif i==2 :
                if (self.button3_back.configure().get('style').__contains__("unchosen.TButton")) and self.button3_front.configure().get('style').__contains__("unchosen.TButton"):
                    self.button3_back.configure(style="blank.TButton")
                    self.button3_front.configure(style="blank.TButton")
                elif (self.button3_back.configure().get('style').__contains__("chosen.TButton")) and self.button3_front.configure().get('style').__contains__("chosen.TButton"):
                    self.button3_back.configure(style="blank.TButton")
                    self.button3_front.configure(style="blank.TButton")
            elif i==3 :
                if (self.button4_back.configure().get('style').__contains__("unchosen.TButton")) and self.button4_front.configure().get('style').__contains__("unchosen.TButton"):
                    self.button4_back.configure(style="blank.TButton")
                    self.button4_front.configure(style="blank.TButton")
                elif (self.button4_back.configure().get('style').__contains__("chosen.TButton")) and self.button4_front.configure().get('style').__contains__("chosen.TButton"):
                    self.button4_back.configure(style="blank.TButton")
                    self.button4_front.configure(style="blank.TButton")
            elif i==4 :
                if (self.button5_back.configure().get('style').__contains__("unchosen.TButton")) and self.button5_front.configure().get('style').__contains__("unchosen.TButton"):
                    self.button5_back.configure(style="blank.TButton")
                    self.button5_front.configure(style="blank.TButton")
                elif (self.button5_back.configure().get('style').__contains__("chosen.TButton")) and self.button5_front.configure().get('style').__contains__("chosen.TButton"):
                    self.button5_back.configure(style="blank.TButton")
                    self.button5_front.configure(style="blank.TButton")


class DefaillanceLouis:

    def __init__(self, master,Elevator):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.Elevator = Elevator

        self.master.title('Defaillances Louis')

        self.button1 = ttk.Button(self.frame, text='fermer les portes manuellement', command=self.fPortes)
        self.button1.pack()
        self.button2 = ttk.Button(self.frame, text='ouvrir les portes manuellement', command=self.ouvPortes)
        self.button2.pack()
        self.button3 = ttk.Button(self.frame, text='ouvrir un peu les portes manuellement', command=self.ouvUnPeuPortes)
        self.button3.pack()
        self.button4 = ttk.Button(self.frame, text='bloquer les portes', command=self.bloquerPortes)
        self.button4.configure(style="unchosen_new.TButton")
        self.button4.pack()
        self.button5 = ttk.Button(self.frame, text='debloquer les portes manuellement', command=self.debloquerPortes)
        self.button5.pack()
        self.button6 = ttk.Button(self.frame, text='l\'ascenceur bouge avec les portes ouvertes',command=self.bougePortesOuvertes)
        self.button6.configure(style="unchosen_new.TButton")
        self.button6.pack()
        self.button7 = ttk.Button(self.frame, text='activer / désactiver la défaillance mauvais étage',command=self.def2)
        self.button7.configure(style="unchosen_new.TButton")
        self.button7.pack()

        self.frame.pack()

        self.frame.pack()

    def def2(self):
        global mauvaisetage
        if mauvaisetage == False:
            mauvaisetage = True
            self.button7.configure(style="chosen_new.TButton")
        else:
            mauvaisetage = False
            self.button7.configure(style="unchosen_new.TButton")

    def fPortes(self):
        global portes_ouvertes, curMouvement
        portes_ouvertes = 0
        if curMouvement=='p':
            curMouvement='0'

            statut = portes[curEtage - 1]
            if mauvaisePorte == True:
                if statut == 0:
                    statut = 1
                else:
                    statut = 0
            Elevator.Door_To_Red(self.Elevator,curEtage, statut)



    def ouvPortes(self):
        global portes_ouvertes, curMouvement
        portes_ouvertes = 1
        if curMouvement!='p':
            curMouvement='p'
            statut = portes[curEtage - 1]
            if mauvaisePorte == True:
                if statut == 0:
                    statut = 1
                else:
                    statut = 0
            Elevator.Door_To_Green(self.Elevator,curEtage, statut)


    def ouvUnPeuPortes(self):
        global portes_ouvertes, PORTES_UN_PEU_OUVERTES
        portes_ouvertes = PORTES_UN_PEU_OUVERTES
        print("portes ouvertes à " + str(PORTES_UN_PEU_OUVERTES * 100) + "%")

    def bloquerPortes(self):
        global portes_bloquees
        portes_bloquees = True
        self.button4.configure(style="chosen_new.TButton")

    def debloquerPortes(self):
        global portes_bloquees
        portes_bloquees = False
        self.button4.configure(style="unchosen_new.TButton")

    def bougePortesOuvertes(self):
        global bouge_portes_ouvertes
        if bouge_portes_ouvertes==False :
            bouge_portes_ouvertes = True
            self.button6.configure(style="chosen_new.TButton")

        else :
            bouge_portes_ouvertes = False
            self.button6.configure(style="unchosen_new.TButton")


class Double_porte_Elio :

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.portes = [0,0,0,0,0] # 0 -> porte de gauche programmée, sinon 1 -> porte de droite. (état initial), chaque indice représente un étage.
        global portes
        self.master.geometry('215x260')
        portes = self.portes

        self.master.title('Defaillances double portes Elio')

        self.display = tk.Label(self.frame, text='Choose on which side the door is')
        self.display.pack()

        plus = ttk.Style()

        plus.map("chosen_new.TButton", foreground=[('pressed', 'green'), ('active', 'silver'),('!disabled','green')],background=[('pressed', '!disabled', 'green')] )
        plus.map("unchosen_new.TButton", foreground=[('pressed', 'firebrick'), ('active', 'silver'),('!disabled','firebrick')],background=[('pressed', '!disabled', 'green')])

        plus.configure("TButton", padding=(0, 5, 0, 5))
        plus.configure("chosen.TButton",foreground='green')
        plus.configure("unchosen.TButton", foreground='firebrick')
        plus.configure("blank.TButton", foreground='black')

        # ----------------------(Buttons 5)---------------------- #
        self.frame5 = tk.Frame(self.frame)
        self.button5L = ttk.Button(self.frame5, text='Left')
        self.button5R = ttk.Button(self.frame5, text='Right')
        self.button5R.configure(command=self.porte_R5)
        self.button5L.configure(command=self.porte_L5)
        self.display_5 = tk.Label(self.frame5, text='  #_5_#  ')

        self.button5L.pack(side=tk.LEFT)
        self.button5R.pack(side=tk.RIGHT)
        self.display_5.pack(side=tk.RIGHT)
        self.frame5.pack(expand=True)
        # ----------------------(Buttons 4)---------------------- #
        self.frame4 = tk.Frame(self.frame)
        self.button4L = ttk.Button(self.frame4, text='Left')
        self.button4R = ttk.Button(self.frame4, text='Right')
        self.button4R.configure(command=self.porte_R4)
        self.button4L.configure(command=self.porte_L4)
        self.display_4 = tk.Label(self.frame4, text='  #_4_#  ')

        self.button4L.pack(side=tk.LEFT)
        self.button4R.pack(side=tk.RIGHT)
        self.display_4.pack(side=tk.RIGHT)
        self.frame4.pack(expand=True)
        # ----------------------(Buttons 3)---------------------- #
        self.frame3 = tk.Frame(self.frame)
        self.button3L = ttk.Button(self.frame3, text='Left')
        self.button3R = ttk.Button(self.frame3, text='Right')
        self.button3R.configure(command=self.porte_R3)
        self.button3L.configure(command=self.porte_L3)
        self.display_3 = tk.Label(self.frame3, text='  #_3_#  ')

        self.button3L.pack(side=tk.LEFT)
        self.button3R.pack(side=tk.RIGHT)
        self.display_3.pack(side=tk.RIGHT)
        self.frame3.pack(expand=True)
        # ----------------------(Buttons 2)---------------------- #
        self.frame2 = tk.Frame(self.frame)
        self.button2L = ttk.Button(self.frame2, text='Left')
        self.button2R = ttk.Button(self.frame2, text='Right')
        self.button2R.configure(command=self.porte_R2)
        self.button2L.configure(command=self.porte_L2)
        self.display_2 = tk.Label(self.frame2, text='  #_2_#  ')

        self.button2L.pack(side=tk.LEFT)
        self.button2R.pack(side=tk.RIGHT)
        self.display_2.pack(side=tk.RIGHT)
        self.frame2.pack(expand=True)
        # ----------------------(Buttons 1)---------------------- #
        self.frame1 = tk.Frame(self.frame)
        self.button1L = ttk.Button(self.frame1, text='Left')
        self.button1R = ttk.Button(self.frame1, text='Right')
        self.button1R.configure(command=self.porte_R1)
        self.button1L.configure(command=self.porte_L1)
        self.display_1 = tk.Label(self.frame1, text='  #_1_#  ')

        self.button1L.pack(side=tk.LEFT)
        self.button1R.pack(side=tk.RIGHT)
        self.display_1.pack(side=tk.RIGHT)
        self.frame1.pack(expand=True)

        self.button_mauvaisePorte = ttk.Button(self.frame, text='l\'ascenceur n\'ouvre pas la bonne porte',command=self.mauvaisePorte)
        self.button_mauvaisePorte.pack()

        self.button_bonnePorte = ttk.Button(self.frame, text='l\'ascenceur ouvre la bonne porte',command=self.bonnePorte)
        self.button_bonnePorte.pack()

        self.porte_L1()
        self.porte_L2()
        self.porte_L3()
        self.porte_L4()
        self.porte_L5()
        self.bonnePorte()

        self.frame.pack()

    def mauvaisePorte(self):
        global mauvaisePorte
        mauvaisePorte = True
        self.button_color(self.button_mauvaisePorte,self.button_bonnePorte)


    def bonnePorte(self):
        global mauvaisePorte
        mauvaisePorte = False
        self.button_color(self.button_bonnePorte,self.button_mauvaisePorte)

    def button_color(self,buttonv,buttonuv):
        buttonv.configure(style="chosen_new.TButton")
        buttonuv.configure(style='unchosen_new.TButton')

    def porte_R1(self):
        self.portes[0]=1
        self.button_color(self.button1R,self.button1L)

    def porte_L1(self):
        self.portes[0]=0
        self.button_color(self.button1L,self.button1R)

    def porte_R2(self):
        self.portes[1]=1
        self.button_color(self.button2R,self.button2L)

    def porte_L2(self):
        self.portes[1]=0
        self.button_color(self.button2L,self.button2R)

    def porte_R3(self):
        self.portes[2]=1
        self.button_color(self.button3R,self.button3L)

    def porte_L3(self):
        self.portes[2]=0
        self.button_color(self.button3L,self.button3R)

    def porte_R4(self):
        self.portes[3]=1
        self.button_color(self.button4R,self.button4L)

    def porte_L4(self):
        self.portes[3]=0
        self.button_color(self.button4L,self.button4R)

    def porte_R5(self):
        self.portes[4]=1
        self.button_color(self.button5R,self.button5L)

    def porte_L5(self):
        self.portes[4]=0
        self.button_color(self.button5L,self.button5R)

def main():
    root = tk.Tk()
    app = Lift(root)
    root.protocol("WM_DELETE_WINDOW", app.sortir)
    Cron = MyTimer(0.02, app.move)
    Cron.start()
    root.mainloop()


if __name__ == '__main__':
    main()
