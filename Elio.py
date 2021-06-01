#!/opt/local/bin/python

import tkinter as tk
import tkinter.ttk as ttk
import time
import sys
from random import randint

import threading

globstop = 0


class MyTimer:
    global globstop
    
    def __init__(self, tempo, target, args= [], kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo
    
    def _run(self):
        if globstop :
            self.exit()
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)
    
    def start(self):
        
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
    
    def stop(self):
        self._timer.cancel()


class Lift():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('ascenseur')


        self.CreerEtage()
        self.CreerElevator()
        self.CreerPortes()

        self.buttonA = tk.Button(self.frame, text = 'Alarm')
        self.buttonA.pack()

        self.button5 = tk.Button(self.frame, text = '5',command=self.Aller5)
        self.button5.pack()
        self.button4 = tk.Button(self.frame, text = '4',command=self.Aller4)
        self.button4.pack()
        self.button3 = tk.Button(self.frame, text = '3',command=self.Aller3)
        self.button3.pack()
        self.button2 = tk.Button(self.frame, text = '2',command=self.Aller2)
        self.button2.pack()
        self.button1 = tk.Button(self.frame, text = '1',command=self.Aller1)
        self.button1.pack()

        self.frame.pack()

        self.CurEtage=1
        self.curMouvement='0'
        self.target=[0,0,0,0,0]
        self.CurPos=0
        self.CurServed=0
        self.CurTempo=0

    def Aller5(self):
        if self.CurPos < 5 :
            self.target[self.CurPos]=5
            self.CurPos = self.CurPos+1
            if self.CurPos==5:
                self.CurPos=0

    def Aller4(self):
        if self.CurPos < 5 :
            self.target[self.CurPos]=4
            self.CurPos = self.CurPos+1
            if self.CurPos==5:
                self.CurPos=0

    def Aller3(self):
        if self.CurPos < 5 :
            self.target[self.CurPos]=3
            self.CurPos = self.CurPos+1
            if self.CurPos==5:
                self.CurPos=0

    def Aller2(self):
        if self.CurPos < 5 :
            self.target[self.CurPos]=2
            self.CurPos = self.CurPos+1
            if self.CurPos==5:
                self.CurPos=0

    def Aller1(self):
        if self.CurPos < 5 :
            self.target[self.CurPos]=1
            self.CurPos = self.CurPos+1
            if self.CurPos==5:
                self.CurPos=0



    def CreerEtage(self):
        self.newWindow = tk.Toplevel(self.master)
        self.Etages = Etages(self.newWindow,self)

    def CreerPortes(self):
        self.newWindow = tk.Toplevel(self.master)
        self.Etages = Double_porte_Elio(self.newWindow, self)

    def CreerElevator(self):

        self.newWindow = tk.Toplevel(self.master)
        self.Elevator = Elevator(self.newWindow)

    def move(self):
# comment out for exam
#        print self.curMouvement
#        print self.CurEtage
#        print self.CurTempo
#        print self.CurPos, self.CurServed
#        print self.target

        if self.CurEtage > 5:
            self.CurEtage=5
            self.curMouvement='0'
        if self.CurEtage < 1:
            self.CurEtage=1
            self.curMouvement='0'

        if self.curMouvement == '+' or self.curMouvement=='-' or self.curMouvement== 'p':
            self.CurTempo=self.CurTempo+1
        if self.CurTempo == 50 or self.CurTempo==0:
            
            if self.curMouvement=='p':
                self.curMouvement='0'
            

            if self.curMouvement=='+':
                self.CurEtage=self.CurEtage+1
                if self.CurEtage==self.target[self.CurServed]:
                    self.curMouvement='p'
                    self.target[self.CurServed]=0
                    self.CurServed=self.CurServed+1
                    if self.CurServed==5:
                        self.CurServed=0
                        #self.target[self.CurPos]=randint(0,5)
                        self.target[self.CurServed] = 0
            if self.curMouvement=='-':
                self.CurEtage=self.CurEtage-1
                if self.CurEtage==self.target[self.CurServed]:
                    self.curMouvement='p'
                    self.target[self.CurServed]=0
                    self.CurServed=self.CurServed+1
                    if self.CurServed==5:
                        self.CurServed=0
                        #self.target[self.CurServed]=randint(0,5)
                        self.target[self.CurServed] = 0

            self.UpdateColor()
            self.CurTempo=0


        if self.curMouvement=='0':
            if self.target[self.CurServed]>0:
                if self.CurEtage < self.target[self.CurServed]:
                    self.curMouvement='+'
                    self.UpdateColor()
                if self.CurEtage >self.target[self.CurServed]:
                    self.curMouvement='-'
                    self.UpdateColor()
                if self.target[self.CurServed]==self.CurEtage:
                    if self.CurServed==4:
                        self.CurServed=0
                    else:
                        self.CurServed=self.CurServed+1
    
                        
    def UpdateColor(self):
#        print "UpdateColor", self.curMouvement, self.CurEtage
        self.Elevator.check_Changes()
        if self.curMouvement=='0':
            if self.CurEtage == 1:
                self.Elevator.Rouge1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 2:
                self.Elevator.Noir1()
                self.Elevator.Rouge2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Rouge3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Rouge4()
                self.Elevator.Noir5()
            if self.CurEtage == 5:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Rouge5()
            self.Elevator.Door_To_Red(self.CurEtage, portes[self.CurEtage-1])



        if self.curMouvement=='p':
            if self.CurEtage == 1:
                self.Elevator.Vert1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 2:
                self.Elevator.Noir1()
                self.Elevator.Vert2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Vert3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Vert4()
                self.Elevator.Noir5()
            if self.CurEtage == 5:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Vert5()
            self.Elevator.Door_To_Green(self.CurEtage, portes[self.CurEtage-1])


        if self.curMouvement=='+':
            if self.CurEtage == 1:
                self.Elevator.Orange1()
                self.Elevator.Bleu2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 2:
                self.Elevator.Noir1()
                self.Elevator.Orange2()
                self.Elevator.Bleu3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Orange3()
                self.Elevator.Bleu4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Orange4()
                self.Elevator.Bleu5()


        if self.curMouvement=='-':
            if self.CurEtage == 2:
                self.Elevator.Bleu1()
                self.Elevator.Orange2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Bleu2()
                self.Elevator.Orange3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Bleu3()
                self.Elevator.Orange4()
                self.Elevator.Noir5()
            if self.CurEtage == 5:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Bleu4()
                self.Elevator.Orange5()

    def sortir(self):
        global globstop
        globstop = 1
        sys.exit(1)


class Etages(Lift):
    def __init__(self, master,Lift):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('Etages')

        self.button5u=tk.Button(self.frame,text='5 ^',command=Lift.Aller5)
        self.button5u.pack()
        self.button5d=tk.Button(self.frame,text='5 v',command=Lift.Aller5)
        self.button5d.pack()

        self.button4u=tk.Button(self.frame,text='4 ^',command=Lift.Aller4)
        self.button4u.pack()
        self.button4d=tk.Button(self.frame,text='4 v',command=Lift.Aller4)
        self.button4d.pack()

        self.button3u=tk.Button(self.frame,text='3 ^',command=Lift.Aller3)
        self.button3u.pack()
        self.button3d=tk.Button(self.frame,text='3 v',command=Lift.Aller3)
        self.button3d.pack()

        self.button2u=tk.Button(self.frame,text='2 ^',command=Lift.Aller2)
        self.button2u.pack()
        self.button2d=tk.Button(self.frame,text='2 v',command=Lift.Aller2)
        self.button2d.pack()

        self.button1u=tk.Button(self.frame,text='1 ^',command=Lift.Aller1)
        self.button1u.pack()
        self.button1d=tk.Button(self.frame,text='1 v',command=Lift.Aller1)
        self.button1d.pack()


        self.master.geometry("+200+200")

        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

class Double_porte_Elio(Lift) :

    def __init__(self, master,Lift):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.portes = [0,0,0,0,0] # 0 -> porte de gauche programmée, sinon 1 -> porte de droite. (état initial), chaque indice représente un étage.
        global portes
        portes = self.portes

        def getPortes():
            return self.portes

        self.master.title('Defaillances double portes Elio')

        self.display = tk.Label(self.frame, text='Choose on which side the door is')
        self.display.pack()

        plus = ttk.Style()
        plus.configure("TButton", padding=(0, 5, 0, 5))
        plus.configure("chosen.TButton",foreground='green')
        plus.configure("unchosen.TButton", foreground='red')
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
        self.porte_L1()
        self.porte_L2()
        self.porte_L3()
        self.porte_L4()
        self.porte_L5()


        self.frame.pack()

    def button_color(self,buttonv,buttonuv):
        buttonv.configure(style="chosen.TButton")
        buttonuv.configure(style='unchosen.TButton')

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



class Elevator:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        #self.new_window = tk.Toplevel(self.master)
        #self.portes = Double_porte(self.new_window,Lift)

        self.master.title('Position')

        style=ttk.Style()
        style.configure("TButton",padding=(0,5,0,5)) 

        style.configure("Red.TButton",foreground='red')
        style.configure("Blue.TButton",foreground='blue')
        style.configure("Green.TButton",foreground='green')
        style.configure("Orange.TButton",foreground='orange')
        style.configure("Black.Tbutton",foreground='black')

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

        self.button4 = ttk.Button(self.frame4, text = '#_4_#')
        self.button4_back = ttk.Button(self.frame4, text='B4')
        self.button4_front = ttk.Button(self.frame4, text='F4')

        self.button4_back.pack(side=tk.LEFT)
        self.button4_front.pack(side=tk.RIGHT)
        self.button4.pack(side=tk.RIGHT)


        self.button4.configure(style="Blue.TButton")

        self.frame4.pack(expand=True)
# ----------------------(Buttons 3)---------------------- #

        self.frame3 = tk.Frame(self.frame)

        self.button3 = ttk.Button(self.frame3, text = '#_3_#')
        self.button3_back = ttk.Button(self.frame3, text='B3')
        self.button3_front = ttk.Button(self.frame3, text='F3')

        self.button3_back.pack(side=tk.LEFT)
        self.button3_front.pack(side=tk.RIGHT)
        self.button3.pack(side=tk.RIGHT)

        self.button3.configure(style="Green.TButton")

        self.frame3.pack(expand=True)
# ----------------------(Buttons 2)---------------------- #

        self.frame2 = tk.Frame(self.frame)

        self.button2 = ttk.Button(self.frame2, text = '#_2_#')
        self.button2_back = ttk.Button(self.frame2, text='B2')
        self.button2_front = ttk.Button(self.frame2, text='F2')

        self.button2_back.pack(side=tk.LEFT)
        self.button2_front.pack(side=tk.RIGHT)
        self.button2.pack(side=tk.RIGHT)

        self.button2.configure(style="Orange.TButton")

        self.frame2.pack(expand=True)
# ----------------------(Buttons 1)---------------------- #
        self.frame1 = tk.Frame(self.frame)

        self.button1 = ttk.Button(self.frame1, text = '#_1_#')
        self.button1_back = ttk.Button(self.frame1, text='B1')
        self.button1_front = ttk.Button(self.frame1, text='F1')

        self.button1.configure(style="Black.TButton")

        self.button1_back.pack(side=tk.LEFT)
        self.button1_front.pack(side=tk.RIGHT)
        self.button1.pack(side=tk.RIGHT)

        self.frame1.pack(expand=True)
        self.master.geometry("+400+400")

        self.frame.pack()

    def Rouge5(self):

        self.button5.configure(style="Red.TButton")
        self.button5.pack()

    def Bleu5(self):
    
        self.button5.configure(style="Blue.TButton")
        self.button5.pack()
    
    def Vert5(self):
        
        self.button5.configure(style="Green.TButton")
        self.button5.pack()

    def Orange5(self):
        
        self.button5.configure(style="Orange.TButton")
        self.button5.pack()
    
    def Noir5(self):
        
        self.button5.configure(style="Black.TButton")
        self.button5.pack()


    def Rouge4(self):
    
        self.button4.configure(style="Red.TButton")
        self.button4.pack()

    def Bleu4(self):
    
        self.button4.configure(style="Blue.TButton")
        self.button4.pack()

    def Vert4(self):
    
        self.button4.configure(style="Green.TButton")
        self.button4.pack()

    def Orange4(self):
    
        self.button4.configure(style="Orange.TButton")
        self.button4.pack()

    def Noir4(self):
    
        self.button4.configure(style="Black.TButton")
        self.button4.pack()


    def Rouge3(self):
    
        self.button3.configure(style="Red.TButton")
        self.button3.pack()

    def Bleu3(self):
    
        self.button3.configure(style="Blue.TButton")
        self.button3.pack()

    def Vert3(self):
    
        self.button3.configure(style="Green.TButton")
        self.button3.pack()

    def Orange3(self):
    
        self.button3.configure(style="Orange.TButton")
        self.button3.pack()

    def Noir3(self):
    
        self.button3.configure(style="Black.TButton")
        self.button3.pack()


    def Rouge2(self):
    
        self.button2.configure(style="Red.TButton")
        self.button2.pack()

    def Bleu2(self):
    
        self.button2.configure(style="Blue.TButton")
        self.button2.pack()

    def Vert2(self):
    
        self.button2.configure(style="Green.TButton")
        self.button2.pack()

    def Orange2(self):
    
        self.button2.configure(style="Orange.TButton")
        self.button2.pack()

    def Noir2(self):
    
        self.button2.configure(style="Black.TButton")
        self.button2.pack()

    def Rouge1(self):
        
    
        self.button1.configure(style="Red.TButton")
        self.button1.pack()

    def Bleu1(self):
    
        self.button1.configure(style="Blue.TButton")
        self.button1.pack()

    def Vert1(self):
    
        self.button1.configure(style="Green.TButton")
        self.button1.pack()

    def Orange1(self):
    
        self.button1.configure(style="Orange.TButton")
        self.button1.pack()

    def Noir1(self):
    
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




def main(): 
    root = tk.Tk()
    app = Lift(root)
    root.protocol("WM_DELETE_WINDOW", app.sortir)
    Cron=MyTimer(0.02,app.move)
    Cron.start()
    root.mainloop()

if __name__ == '__main__':
    main()
