###ChangeLog
###Version 0.002: New release, overhauled code to include and accomidate User Interface.
###Version 0.001.6.U: Simplified regulate, reduced the number of lists. Lists now clear at the end of regulate.
###Version 0.001.5.U: After many attempts, the problem with the temperature regulation was found to be in deyeat. Unreleased.
####deyeat's execution order triggered regulate before flipping the valve to 'open'.
####This meant that determineflow and thermalize would not get past "if self.status == 'open'".
###Version 0.001: First release, added classes and objects, and a nonfunctioning temperature regulation system.
###Version 0.000.U: Original version, unreleased.

from statistics import mean
from typing import List
from random import randint

##Having my lists as objects is *probably* unneccessary, but I haven't bothered fixing it yet.
class StringRecepticle(object):
    def __init__(self, name):
        self.name = name
        self.held: List[str] = []
    def add_hold(self, hold):
        self.held.append(hold)

class IntegerRecepticle(object):
    def __init__(self, name):
        self.name = name
        self.held: List[int] = []
    def add_hold(self, hold):
        self.held.append(hold)

class ListPocket(object):
    def __init__(self):
        self.held: List = []
    def add_hold(self, hold):
        self.held.append(hold)

alpha = StringRecepticle('alpha')
beta = StringRecepticle('beta')
gamma = StringRecepticle('gamma')
delta = IntegerRecepticle('delta')
#zeta = StringRecepticle('zeta')
#eta = StringRecepticle('eta')
#theta = StringRecepticle('theta')
#epsilon = list() #unused
#iota = list() #unused



def regulate (self):
    determineflow(self)
    for x in alpha.held:
        thermalize(x)
    for y in beta.held:
        thermalize(y)
    alpha.held = []
    beta.held = []
    gamma.held = []
    delta.held = []

def wincheck():
    if len(gamma.held) == 2:
        print("\u001b[33mYou Win!")
        input("Press any key to continue")
        main()

def determineflow (self): #Runs a 'search' that starts at the chosen component, storing their temperature.
    if self not in self.firstlist.held: #Prevents back-and-forths and other endless loops.
        if self.status == 'open':
            if self.tag == 'valve':
                self.firstlist.add_hold(self)
                self.thirdlist.add_hold(self.temperature)
                if self.firstforwardconnection != None:
                    determineflow(self.firstforwardconnection)
                if self.secondforwardconnection != None:
                    determineflow(self.secondforwardconnection)
                if self.firstbackwardconnection != None:
                    determineflow(self.firstbackwardconnection)
                if self.secondbackwardconnection != None:
                    determineflow(self.secondbackwardconnection)
            if self.tag == 'vein':
                self.firstlist.add_hold(self)
                self.thirdlist.add_hold(self.temperature)
                if self.forwardconnection != None:
                    determineflow(self.forwardconnection)
                if self.backwardconnection != None:
                    determineflow(self.backwardconnection)
            if self.tag == 'heart':
                self.firstlist.add_hold(self)
                self.thirdlist.add_hold(self.temperature)
                if self.firstforwardconnection != None:
                    determineflow(self.firstforwardconnection)
                if self.secondforwardconnection != None:
                    determineflow(self.secondforwardconnection)
                if self.firstbackwardconnection != None:
                    determineflow(self.firstbackwardconnection)
                if self.secondbackwardconnection != None:
                    determineflow(self.secondbackwardconnection)

def thermalize(self): #Applies the average temperature of the connected. Yes, I could just make make a for-loop using alpha.
    self.temperature = mean(self.thirdlist.held)
    self.colorize()

def yeat(count, value): #this method performs the math
    if count>0:
        count = count + value
    return count

def deyeat(self, value):
    if self.status =='open': #if a valve is open, apply the math to the open timer
        self.currenttime = yeat(self.currenttime,value)
        if self.currenttime <= 0: #if the valve's open timer runs out, this flips the valve closed, without timer runoff.
            self.status ='closed'    
            self.currenttime = int(round(self.temperature)) + self.baseclosedtime #placeholder calculation
    if self.status =='closed': #if a valve is closed, apply the math to the closed timer
        self.currenttime = yeat(self.currenttime,value)
        if self.currenttime <= 0: #if the valve's closed timer runs out, this flips the valve open, without timer runoff.
            #insert temperature averager method here.
            self.status ='open'
            regulate(self) 
            self.currenttime = self.baseopentime - int(round(self.temperature)) #placeholder calculation

def beat(): #subtracts 1 from the active timer of every valve
    for x in valvelist.held:
        deyeat(x,-1) #iterates for each valve
        x.colorize()
    for x in veinlist.held:
        x.colorize()
    
class Valve(object):
    def __init__(self, name, tag, status, temperature, currenttime, baseopentime, baseclosedtime, firstforwardconnection, secondforwardconnection, firstbackwardconnection, secondbackwardconnection, firstlist, secondlist, thirdlist, sign):
        self.name = name
        self.tag = tag
        self.status = status #Is the valve "open" or "closed".
        self.temperature = float(temperature)
        self.currenttime = float(currenttime)
        self.baseopentime = float(baseopentime)
        self.baseclosedtime = float(baseclosedtime)
        self.firstforwardconnection = firstforwardconnection
        self.secondforwardconnection = secondforwardconnection
        self.firstbackwardconnection = firstbackwardconnection
        self.secondbackwardconnection = secondbackwardconnection
        self.firstlist = firstlist
        self.secondlist = secondlist
        self.thirdlist = thirdlist
        self.sign = sign
        self.colorize()
    def colorize(self):
        if self.currenttime <= 9:
            temp = " " + str(self.currenttime)
        else:
            temp = str(self.currenttime)
        if self.status == "open":
            self.upper = "\033[1;37;40mO"
            self.lower = "\033[1;37;40m" + temp
        elif self.status == "closed":
            self.upper = "\033[1;37;40mX"
            self.lower = "\033[1;37;40m" + temp
        if 0 <= self.temperature <= 1:
            self.signcolor = "\033[1;31;40m" + self.sign
        elif 1 <= self.temperature <= 2:
            self.signcolor = "\033[1;35;40m" + self.sign
        elif 2 <= self.temperature <= 3:
            self.signcolor = "\033[1;34;40m" + self.sign
        elif 3 <= self.temperature <= 4:
            self.signcolor = "\033[1;36;40m" + self.sign

class Vein(object):
    def __init__(self, name, tag, status, temperature, forwardconnection, backwardconnection, firstlist, secondlist, thirdlist, sign):
        self.name = name
        self.tag = tag
        self.status = status #Vein statuses are always "open"
        self.temperature = float(temperature)
        self.forwardconnection = forwardconnection
        self.backwardconnection = backwardconnection
        self.firstlist = firstlist
        self.secondlist = secondlist
        self.thirdlist = thirdlist
        self.sign = sign
        self.colorize()
    def colorize(self):
        if 0 <= self.temperature <= 1:
            self.signcolor = "\033[1;31;40m" + self.sign
        elif 1 <= self.temperature <= 2:
            self.signcolor = "\033[1;35;40m" + self.sign
        elif 2 <= self.temperature <= 3:
            self.signcolor = "\033[1;34;40m" + self.sign
        elif 3 <= self.temperature <= 4:
            self.signcolor = "\033[1;36;40m" + self.sign
        
class Heart(object):
    def __init__(self, name, tag, status, temperature, firstforwardconnection, secondforwardconnection, firstbackwardconnection, secondbackwardconnection, firstlist, secondlist, thirdlist, sign):
        self.name = name
        self.tag = tag
        self.status = status
        self.temperature = float(temperature)
        self.firstforwardconnection = firstforwardconnection
        self.secondforwardconnection = secondforwardconnection
        self.firstbackwardconnection = firstbackwardconnection
        self.secondbackwardconnection = secondbackwardconnection
        self.firstlist = firstlist
        self.secondlist = secondlist
        self.thirdlist = thirdlist
        self.sign = sign
    def colorize(self):
        if 0 <= self.temperature <= 1:
            self.signcolor = "\033[1;31;40m" + self.sign
        elif 1 <= self.temperature <= 2:
            self.signcolor = "\033[1;35;40m" + self.sign
        elif 2 <= self.temperature <= 3:
            self.signcolor = "\033[1;34;40m" + self.sign
        elif 3 <= self.temperature <= 4:
            self.signcolor = "\033[1;36;40m" + self.sign

# Prior declarations of objects and functions declared after-the-fact that may cause issues due to not being defined.
valvelist = ListPocket()
veinlist = ListPocket()
def export():
    pass


menudict={
    "1":1,
    "2":2,
    "3":3
}



def main():
    print("Welcome to Fever Hearts")
    print("Press [1] for easy spread")
    print("Press [2] for difficult spread")
    print("Press [3] for instructions")

    x = input()
    while x not in menudict:
        print("Error! This is not a proper input. Try again.")
        x = input()
    else:
        if menudict[x] == 1:
            #setup:
            #IMPORTANT: ALL VARIABLES MUST BE DECLARED BEFORE CONNECTIONS CAN BE ESTABLISHED.
            HisHeart = Heart('HisHeart','heart',None,'0',None,None,None,None,gamma,None,delta,"\u2665")
            HerHeart = Heart('HerHeart','heart',None,'0',None,None,None,None,gamma,None,delta,"\u2665")

            HisHeart_A = Vein('HisHeart_A','vein',None,'0',None,None,beta,None,delta,"-")
            A_B = Vein('A_B','vein',None,'0',None,None,beta,None,delta,"/")
            A_C = Vein('A_C','vein',None,'0',None,None,beta,None,delta,"\\")
            B_D = Vein('B_D','vein',None,'0',None,None,beta,None,delta,"\\")
            C_D = Vein('C_D','vein',None,'0',None,None,beta,None,delta,"/")
            D_HerHeart = Vein('D_HerHeart','vein',None,'0',None,None,beta,None,delta,"-")

            A = Valve('A','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"A")
            B = Valve('B','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"B")
            C = Valve('C','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"C")
            D = Valve('D','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"D")

            valvedict={
                "A":A,
                "a":A,
                "B":B,
                "b":B,
                "C":C,
                "c":C,
                "D":D,
                "d":D
            }

            valvelist.add_hold(A)
            valvelist.add_hold(B)
            valvelist.add_hold(C)
            valvelist.add_hold(D)

            veinlist.add_hold(HisHeart_A)
            veinlist.add_hold(A_B)
            veinlist.add_hold(A_C)
            veinlist.add_hold(B_D)
            veinlist.add_hold(C_D)
            veinlist.add_hold(D_HerHeart)

            #Now that variables have been declared, they can be assigned their actual characteristics.
            #hearts
            HisHeart.status = 'open'
            HisHeart.temperature = 1
            HisHeart.firstforwardconnection = HisHeart_A
            HisHeart.secondforwardconnection = None
            HisHeart.firstbackwardconnection = None
            HisHeart.secondbackwardconnection = None
            HisHeart.colorize()

            HerHeart.status = 'open'
            HerHeart.temperature = 4
            HerHeart.firstforwardconnection = None
            HerHeart.secondforwardconnection = None
            HerHeart.firstbackwardconnection = None
            HerHeart.secondbackwardconnection = D_HerHeart
            HerHeart.colorize()

            #veins
            HisHeart_A.status = 'open' 
            HisHeart_A.temperature = 1
            HisHeart_A.forwardconnection = HisHeart
            HisHeart_A.backwardconnection = A
            HisHeart_A.colorize()

            A_B.status = 'open' 
            A_B.temperature = 2
            A_B.forwardconnection = A
            A_B.backwardconnection = B
            A_B.colorize()

            A_C.status = 'open' 
            A_C.temperature = 2
            A_C.forwardconnection = A
            A_C.backwardconnection = C
            A_C.colorize()

            B_D.status = 'open' 
            B_D.temperature = 3
            B_D.forwardconnection = B
            B_D.backwardconnection = D
            B_D.colorize()

            C_D.status = 'open' 
            C_D.temperature = 3
            C_D.forwardconnection = C
            C_D.backwardconnection = D
            C_D.colorize()

            D_HerHeart.status = 'open' 
            D_HerHeart.temperature = 4
            D_HerHeart.forwardconnection = D
            D_HerHeart.backwardconnection = HerHeart
            D_HerHeart.colorize()

            #valves
            A.status = 'closed'
            A.temperature = 2
            A.baseopentime = 5
            A.baseclosedtime = 5
            A.currenttime = randint(1, int(round(5-A.temperature))+A.baseclosedtime)
            A.firstforwardconnection = HisHeart_A
            A.secondforwardconnection = None
            A.firstbackwardconnection = A_B
            A.secondbackwardconnection = A_C
            A.colorize()

            B.status = 'closed'
            B.temperature = 3
            B.baseopentime = 5
            B.baseclosedtime = 5
            B.currenttime = randint(1, int(round(5-B.temperature))+B.baseclosedtime)
            B.firstforwardconnection = A_B
            B.secondforwardconnection = None
            B.firstbackwardconnection = B_D
            B.secondbackwardconnection = None
            B.colorize()

            C.status = 'closed'
            C.temperature = 3
            C.baseopentime = 5
            C.baseclosedtime = 5
            C.currenttime = randint(1, int(round(5-C.temperature))+C.baseclosedtime)
            C.firstforwardconnection = A_C
            C.secondforwardconnection = None
            C.firstbackwardconnection = C_D
            C.secondbackwardconnection = None
            C.colorize()

            D.status = 'closed'
            D.temperature = 3
            D.baseopentime = 5
            D.baseclosedtime = 5
            D.currenttime = randint(1, int(round(5-D.temperature))+D.baseclosedtime)
            D.firstforwardconnection = B_D
            D.secondforwardconnection = C_D
            D.firstbackwardconnection = D_HerHeart
            D.secondbackwardconnection = None
            D.colorize()

            def easyexport(): #prints gamestate
                print("\033[1;30;40m")
                print("\033[1;30;40m")
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + " " + B.upper)
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + " " + B.signcolor)
                print("\033[1;30;40m " + " " + " " + " " + " " + A.upper + " " + A_B.signcolor + B.lower + " " + B_D.signcolor + " " + D.upper)
                print("\033[1;30;40m " + HisHeart.signcolor + " " + HisHeart_A.signcolor + " " + A.signcolor + " " + " " + " " + " " + " " + " " + " " + D.signcolor + " " + D_HerHeart.signcolor + " " + HerHeart.signcolor)
                print("\033[1;30;40m " + " " + " " + " " + A.lower + " " + A_C.signcolor + " " + C.upper + " " + C_D.signcolor + D.lower)
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + " " + C.signcolor)
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + C.lower)
                print("\033[1;30;40m")
                print("\033[1;30;40m")
                determineflow(HisHeart)
                wincheck()
                x = input()
                while x not in valvedict:
                    print("Error! This is not a number. Try again.")
                    x = input()
                else:
                    deyeat(valvedict[x],-1)
                beat()
                export()
            export = easyexport            
            export()
        elif menudict[x] == 2:
            #setup:
            #IMPORTANT: ALL VARIABLES MUST BE DECLARED BEFORE CONNECTIONS CAN BE ESTABLISHED.
            HisHeart = Heart('HisHeart','heart',None,'0',None,None,None,None,gamma,None,delta,"\u2665")
            HerHeart = Heart('HerHeart','heart',None,'0',None,None,None,None,gamma,None,delta,"\u2665")

            HisHeart_A = Vein('HisHeart_A','vein',None,'0',None,None,beta,None,delta,"-")
            A_B = Vein('A_B','vein',None,'0',None,None,beta,None,delta,"/")
            A_C = Vein('A_C','vein',None,'0',None,None,beta,None,delta,"\\")
            B_D = Vein('B_D','vein',None,'0',None,None,beta,None,delta,"/")
            B_E = Vein('B_E','vein',None,'0',None,None,beta,None,delta,"\\")
            C_E = Vein('C_E','vein',None,'0',None,None,beta,None,delta,"/")
            C_F = Vein('C_F','vein',None,'0',None,None,beta,None,delta,"\\")
            D_G = Vein('D_G','vein',None,'0',None,None,beta,None,delta,"\\")
            E_G = Vein('E_G','vein',None,'0',None,None,beta,None,delta,"/")
            E_H = Vein('E_H','vein',None,'0',None,None,beta,None,delta,"\\")
            F_H = Vein('F_H','vein',None,'0',None,None,beta,None,delta,"/")
            G_I = Vein('G_I','vein',None,'0',None,None,beta,None,delta,"\\")
            H_I = Vein('H_I','vein',None,'0',None,None,beta,None,delta,"/")        
            I_HerHeart = Vein('I_HerHeart','vein',None,'0',None,None,beta,None,delta,"-")

            A = Valve('A','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"A")
            B = Valve('B','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"B")
            C = Valve('C','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"C")
            D = Valve('D','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"D")
            E = Valve('E','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"E")
            F = Valve('F','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"F")
            G = Valve('G','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"G")
            H = Valve('H','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"H")
            I = Valve('I','valve',None,'0','0','0','0',None,None,None,None,alpha,None,delta,"I")

            valvedict={
                "A":A,
                "a":A,
                "B":B,
                "b":B,
                "C":C,
                "c":C,
                "D":D,
                "d":D,
                "E":E,
                "e":E,
                "F":F,
                "f":F,
                "G":G,
                "g":G,
                "H":H,
                "h":H,
                "I":I,
                "i":I
            }


            valvelist.add_hold(A)
            valvelist.add_hold(B)
            valvelist.add_hold(C)
            valvelist.add_hold(D)
            valvelist.add_hold(E)
            valvelist.add_hold(F)
            valvelist.add_hold(G)
            valvelist.add_hold(H)
            valvelist.add_hold(I)

            veinlist.add_hold(HisHeart_A)
            veinlist.add_hold(A_B)
            veinlist.add_hold(A_C)
            veinlist.add_hold(B_D)
            veinlist.add_hold(B_E)
            veinlist.add_hold(C_E)
            veinlist.add_hold(C_F)
            veinlist.add_hold(D_G)
            veinlist.add_hold(E_G)
            veinlist.add_hold(E_H)
            veinlist.add_hold(F_H)
            veinlist.add_hold(G_I)
            veinlist.add_hold(H_I)
            veinlist.add_hold(I_HerHeart)

            #Now that variables have been declared, they can be assigned their actual characteristics.
            #hearts
            HisHeart.status = 'open'
            HisHeart.temperature = 1
            HisHeart.firstforwardconnection = HisHeart_A
            HisHeart.secondforwardconnection = None
            HisHeart.firstbackwardconnection = None
            HisHeart.secondbackwardconnection = None
            HisHeart.colorize()

            HerHeart.status = 'open'
            HerHeart.temperature = 4
            HerHeart.firstforwardconnection = None
            HerHeart.secondforwardconnection = None
            HerHeart.firstbackwardconnection = None
            HerHeart.secondbackwardconnection = I_HerHeart
            HerHeart.colorize()

            #veins
            HisHeart_A.status = 'open' 
            HisHeart_A.temperature = 1
            HisHeart_A.forwardconnection = HisHeart
            HisHeart_A.backwardconnection = A
            HisHeart_A.colorize()

            A_B.status = 'open' 
            A_B.temperature = 2
            A_B.forwardconnection = A
            A_B.backwardconnection = B
            A_B.colorize()

            A_C.status = 'open' 
            A_C.temperature = 2
            A_C.forwardconnection = A
            A_C.backwardconnection = C
            A_C.colorize()

            B_D.status = 'open' 
            B_D.temperature = 3
            B_D.forwardconnection = B
            B_D.backwardconnection = D
            B_D.colorize()

            B_E.status = 'open' 
            B_E.temperature = 3
            B_E.forwardconnection = B
            B_E.backwardconnection = E
            B_E.colorize()

            C_E.status = 'open' 
            C_E.temperature = 3
            C_E.forwardconnection = C
            C_E.backwardconnection = E
            C_E.colorize()

            C_F.status = 'open'
            C_F.temperature = 3
            C_F.forwardconnection = C
            C_F.backwardconnection = F
            C_F.colorize()

            D_G.status = 'open' 
            D_G.temperature = 3
            D_G.forwardconnection = D
            D_G.backwardconnection = G
            D_G.colorize()

            E_G.status = 'open' 
            E_G.temperature = 3
            E_G.forwardconnection = E
            E_G.backwardconnection = G
            E_G.colorize()

            E_H.status = 'open' 
            E_H.temperature = 3
            E_H.forwardconnection = E
            E_H.backwardconnection = H
            E_H.colorize()
            
            F_H.status = 'open' 
            F_H.temperature = 3
            F_H.forwardconnection = F
            F_H.backwardconnection = H
            F_H.colorize()

            G_I.status = 'open' 
            G_I.temperature = 3
            G_I.forwardconnection = G
            G_I.backwardconnection = I
            G_I.colorize()

            H_I.status = 'open' 
            H_I.temperature = 3
            H_I.forwardconnection = H
            H_I.backwardconnection = I
            H_I.colorize()

            I_HerHeart.status = 'open' 
            I_HerHeart.temperature = 4
            I_HerHeart.forwardconnection = I
            I_HerHeart.backwardconnection = HerHeart
            I_HerHeart.colorize()

            #valves
            A.status = 'closed'
            A.temperature = 2
            A.baseopentime = 5
            A.baseclosedtime = 5
            A.currenttime = randint(1, int(round(5-A.temperature))+A.baseclosedtime)
            A.firstforwardconnection = HisHeart_A
            A.secondforwardconnection = None
            A.firstbackwardconnection = A_B
            A.secondbackwardconnection = A_C
            A.colorize()

            B.status = 'closed'
            B.temperature = 3
            B.baseopentime = 5
            B.baseclosedtime = 5
            B.currenttime = randint(1, int(round(5-B.temperature))+B.baseclosedtime)
            B.firstforwardconnection = A_B
            B.secondforwardconnection = None
            B.firstbackwardconnection = B_D
            B.secondbackwardconnection = B_E
            B.colorize()

            C.status = 'closed'
            C.temperature = 3
            C.baseopentime = 5
            C.baseclosedtime = 5
            C.currenttime = randint(1, int(round(5-C.temperature))+C.baseclosedtime)
            C.firstforwardconnection = A_C
            C.secondforwardconnection = None
            C.firstbackwardconnection = C_E
            C.secondbackwardconnection = C_F
            C.colorize()

            D.status = 'closed'
            D.temperature = 3
            D.baseopentime = 5
            D.baseclosedtime = 5
            D.currenttime = randint(1, int(round(5-D.temperature))+D.baseclosedtime)
            D.firstforwardconnection = B_D
            D.secondforwardconnection = None
            D.firstbackwardconnection = D_G
            D.secondbackwardconnection = None
            D.colorize()

            E.status = 'closed'
            E.temperature = 3
            E.baseopentime = 5
            E.baseclosedtime = 5
            E.currenttime = randint(1, int(round(5-E.temperature))+E.baseclosedtime)
            E.firstforwardconnection = E_G
            E.secondforwardconnection = E_H
            E.firstbackwardconnection = B_E
            E.secondbackwardconnection = C_E
            E.colorize()

            F.status = 'closed'
            F.temperature = 3
            F.baseopentime = 5
            F.baseclosedtime = 5
            F.currenttime = randint(1, int(round(5-F.temperature))+F.baseclosedtime)
            F.firstforwardconnection = C_F
            F.secondforwardconnection = None
            F.firstbackwardconnection = F_H
            F.secondbackwardconnection = None
            F.colorize()

            G.status = 'closed'
            G.temperature = 3
            G.baseopentime = 5
            G.baseclosedtime = 5
            G.currenttime = randint(1, int(round(5-F.temperature))+F.baseclosedtime)
            G.firstforwardconnection = G_I
            G.secondforwardconnection = None
            G.firstbackwardconnection = D_G
            G.secondbackwardconnection = E_G
            G.colorize()
        
            H.status = 'closed'
            H.temperature = 3
            H.baseopentime = 5
            H.baseclosedtime = 5
            H.currenttime = randint(1, int(round(5-G.temperature))+G.baseclosedtime)
            H.firstforwardconnection = H_I
            H.secondforwardconnection = None
            H.firstbackwardconnection = E_H
            H.secondbackwardconnection = F_H
            H.colorize()

            I.status = 'closed'
            I.temperature = 3
            I.baseopentime = 5
            I.baseclosedtime = 5
            I.currenttime = randint(1, int(round(5-I.temperature))+I.baseclosedtime)
            I.firstforwardconnection = I_HerHeart
            I.secondforwardconnection = None
            I.firstbackwardconnection = G_I
            I.secondbackwardconnection = H_I
            I.colorize()

            def difficultexport(): #prints gamestate
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + D.upper)
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + D.signcolor)
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + " " + B.upper + " " + B_D.signcolor + D.lower + " " + D_G.signcolor + " " + G.upper)
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + " " + B.signcolor + " " + " " + " " + " " + " " + " " + " " + G.signcolor)
                print("\033[1;30;40m " + " " + " " + " " + " " + A.upper + " " + A_B.signcolor + B.lower + " " + B_E.signcolor + " " + E.upper + " " + E_G.signcolor + G.lower + " " + G_I.signcolor + " " + I.upper)
                print("\033[1;30;40m " + HisHeart.signcolor + " " + HisHeart_A.signcolor + " " + A.signcolor + " " + " " + " " + " " + " " + " " + " " + E.signcolor + " " + " " + " " + " " + " " + " " + " " + I.signcolor + " " + I_HerHeart.signcolor + " " + HerHeart.signcolor)
                print("\033[1;30;40m " + " " + " " + " " + A.lower + " " + A_C.signcolor + " " + C.upper + " " + C_E.signcolor + E.lower + " " + E_H.signcolor + " " + H.upper + " " + H_I.signcolor + I.lower)
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + " " + C.signcolor + " " + " " + " " + " " + " " + " " + " " + H.signcolor)
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + C.lower + " " + C_F.signcolor + " " + F.upper + " "  + F_H.signcolor + H.lower)
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + F.signcolor + " " + " ")
                print("\033[1;30;40m " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + " " + F.lower + " " + " ")
                determineflow(HisHeart)
                wincheck()
                x = input()
                while x not in valvedict:
                    print("Error! This is not a number. Try again.")
                    x = input()
                else:
                    deyeat(valvedict[x],-1)
                beat()
                export()
            export = difficultexport
            export()
        if menudict[x] == 3:
            print("Welcome to the alpha release of Fever Hearts, a puzzle programmed in Python")
            print("as a component of a larger personal project.")
            print("The goal of game is to form a path of open valves (denoted by letters) from one end")
            print("(the 'hot' red heart) to the other (the 'cold' blue heart), as connected by the veins")
            print("(denoted by [/], [\] or [-]).")
            print("Valves")
            print("All valves are closed for a set number of turns, and then open for a set, smaller number of turns.")
            print("These values can be seen below the valve's letter, and are affected by the valve's 'temperature'.")
            print("Above each valve is an [X] (denoting closed) or [O] (denoting open). Below each valve is a number")
            print("denoting how many more turns it will remain closed/open. After every action, every valve's counter")
            print("is reduced by one.")
            print("Temperature")
            print("Every object has a temperature: hot, warm, lukewarm, or cold. Their symbol is colored to demonstrate")
            print("this state. Temperature only affects valves. Whenever a valve opens, the temperature between it, all")
            print("veins connected to it, all open other valves connected to those veins, and so on, are averaged.")
            print("If a heart is connected in this way, its value contributes to the average, but is not changed.")
            print("The colder a valve is, the longer it stays closed, and the shorter it remains open.")
            print("Gameplay")
            print("To play, simply type in the letter (capital or lowercase) of the valve you would like to target,")
            print("and hit [Enter] to submit it. If that valve is closed, its counter will be reduced by one further,")
            print("effectively by two. If that valve is open, then the counter will be increased by one, effectively by zero.")
            print("Use this to your advantage!")
            input("Press any key to continue")
            main()
            
            
main()