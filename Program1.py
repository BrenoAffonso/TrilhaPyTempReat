import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import math 
import random
import time

tIdeal=308 # temperatura ideal        unidade = Kelvin
tCrit=313 # temperatura crítica       unidade = Kelvin 
tEntr=300 # temperatura de entrada    unidade = Kelvin
tReat=300 # temperatura do reator     unidade = Kelvin
tCam=320 # temperatura da camisa      unidade = Kelvin
tMin=290 # temperatura mínima         unidade = Kelvin


fReat=100   #vazão do reator                   unidade = kg/s
fCam=50    # vazão da camisa                   unidade = kg/s
coefG=500000    #coeficiente global                unidade = W/K
cpCam=50   # calor específico da camisa        unidade = j/(Kg * K)
cpReat=150 # calor específico do reator        unidade = j/(Kg * K)
timeCam=1

massReat=10000  # massa do reator     unidade = kg

root = tk.Tk()
root.title("Temperature Warning")
n=1

timeCounter=[]
tempsR=[]
tempsC=[]

while True:
    eReat=tReat*cpReat*massReat     #Energia dentro do reator
    eReat-=tReat*fReat*cpReat       #Energia de F2
    eReat+=tEntr*fReat*cpReat       #Energia de F1

    eReat+=(tCam-tReat)*timeCam*coefG #Energia da camisa

    tReat=eReat/(cpReat*massReat)

    luck=random.randint(0,100)
    if luck==50:
        luck=random.randint(0,100)
        tReat+=luck
    if luck ==51:
        luck=random.randint(0,100)
        tReat-=luck

    eReatIdeal=tIdeal*cpReat*massReat
    eReat=tReat*cpReat*massReat
    
    tCam=tReat-((eReat-eReatIdeal)/(timeCam*coefG))
    


    print(f'Loop {n}')
    print(f'Temperatura do Reator: {tReat}')
    print(f"Temperatura do fluido da camisa: {tCam}")
    tempsR.append(tReat)
    timeCounter.append(n)
    tempsC.append(tCam)

    if tReat>tCrit: 
        messagebox.showwarning("Warning", "Temperature above critical!")
    if tReat<tMin:
        messagebox.showwarning("Warning", "Temperature below minimum!")
    n+=1
    time.sleep(0)
    if n==1000:
        plt.figure(figsize=(8, 5))
        plt.plot(timeCounter, tempsR, marker='o',markersize=1, color='blue')
        plt.plot(timeCounter, tempsC, marker='o',markersize=1, color='red')
        plt.grid()
        plt.show()

