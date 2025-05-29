#importēti TK bibliotēka
#pārdēvēta tkinter par TK lai vieglāk ar to strādātu
import tkinter as Tk
import csv
from tkinter import *
from tkinter import messagebox

#tiek nosaukts un izveidots teksta logs
logs=Tk()
logs.geometry("500x500")

#veido tekstu galveno tekstu
lvards=Label(logs,text=f"Ievadi vārdu:",font=('Arial',8,"bold"))
luzvards=Label(logs,text=f"Ievadi uzvārdu:",font=('Arial',8,"bold"))
lvecums=Label(logs,text=f"Ievadi vecumu:",font=('Arial',8,"bold"))
lepasts=Label(logs,text=f"Ievadi epastu:",font=('Arial',8,"bold"))
llietotajvards=Label(logs,text=f"Ievadi lietotājvārdu:",font=('Arial',8,"bold"))
sigma=Label(logs,text="neesi pilngadīgs!",font=('Arial',8,"bold"))
#veidota metode, ar kuru pogas klikšķienā tiks izpildīta
def click1():
    #tiek iegūti un saglabāti atribūti
    izvade_v=Label(logs,text=ievade_v.get())
    vards=ievade_v.get() 

    izvade_u=Label(logs,text=ievade_u.get())
    uzvards=ievade_u.get()

    izvade_ve=Label(logs,text=ievade_ve.get())
    vecums_str=ievade_ve.get()
    #pārveido vecumu par int
    vecums=int(vecums_str)
    izvade_e=Label(logs,text=ievade_e.get())
    epasts=ievade_e.get()
    
    izvade_l=Label(logs,text=ievade_l.get())
    lietotajs=ievade_l.get()
    #tiek veidota klase
    class Persona():
        def __init__(self,vards,uzvards,vecums,epasts):
            self._vards=vards
            self._uzvards=uzvards
            self._vecums=vecums
            self._epasts=epasts
    #veidota pirmā klases metode, kur pārbauda vecumu
        def a(self):
            if self._vecums>=18:
                print(vards,uzvards,vecums,epasts)
            else:
                print("neesi pilngadīgs!")
        def csv(self):
            if self._vecums>=18:    
                with open("Lietotaji.csv", mode="w",newline="",encoding="utf-8") as file:
                    writer=csv.writer(file)
                    writer.writerow([self._vards,self._uzvards,self._vecums,self._epasts])
            else:
                print("nevareju to saglabaat jo ^^^")
    class Lietotajs(Persona):
        def __init__(self,vards,uzvards,vecums,epasts,lietotajs):

            super().__init__(vards,uzvards,vecums,epasts)
            self.lietotajs=lietotajs
        def a(self):
            if self._vecums>=18:
                print(vards,uzvards,vecums,epasts,self.lietotajs)
            else:
                print("neesi pilngadīgs!")
        def csv(self):
            if self._vecums>=18:
                with open("Lietotaji.csv", mode="w",newline="",encoding="utf-8") as file:
                    writer=csv.writer(file)
                    writer.writerow([self._vards,self._uzvards,self._vecums,self._epasts,self.lietotajs])
            else:
                print("nevareju to saglabaat jo ^^^")
    #izvadīta klase konsolē
    persona=Persona(vards,uzvards,vecums,epasts)
    persona.a()
    persona.csv()
    lietotajv=Lietotajs(vards,uzvards,vecums,epasts,lietotajs)
    lietotajv.a()
    lietotajv.csv()
    #vecuma pārbaude deļ GUI
    if vecums>=18:
        #izvada datus GUI
        izvade_v.pack()
        izvade_u.pack()
        izvade_ve.pack()
        izvade_e.pack()
        izvade_l.pack()
    else:
        sigma.pack()





#tiek veidota poga, kuru nospiežot tiks palaista metode "click"
poga1=Button(text="ok",font=("Arial",10,"bold"), command=click1)

#tiek veidotas ievades lodziņi
ievade_v=Entry()
ievade_u=Entry()
ievade_ve=Entry()
ievade_e=Entry()
ievade_l=Entry()
#parāda vizuāli galveno tekstu, ar tās ievades lodziņiem
lvards.pack()
ievade_v.pack()

luzvards.pack()
ievade_u.pack()

lvecums.pack()
ievade_ve.pack()

lepasts.pack()
ievade_e.pack()

llietotajvards.pack()
ievade_l.pack()

poga1.pack()
#ciklē logu, lai nepārtrauktos
logs.mainloop()
