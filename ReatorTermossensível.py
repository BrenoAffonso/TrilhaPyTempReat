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
tCam=308 # temperatura da camisa      unidade = Kelvin
tMin=290 # temperatura mínima         unidade = Kelvin


fReat=50   #vazão do reator                   unidade = kg/s
fCam=50    # vazão da camisa                   unidade = kg/s
coefG=50000    #coeficiente global                unidade = W/K
cpCam=50   # calor específico da camisa        unidade = j/(Kg * K)
cpReat=150 # calor específico do reator        unidade = j/(Kg * K)
timeCam=1

limVar=0 #Limite do quanto a temperatura da camisa consegue variar em 1 segundo
tCamOld=tCam

failure=0

massReat=10000  # massa do reator     unidade = kg

root = tk.Tk()
root.title("Temperature Warning")
n=1


timeCounter=[]
tempsR=[]
tempsC=[]
failureCounter=[]

while True:
    eReat=tReat*cpReat*massReat     #Energia dentro do reator
    eReat-=tReat*fReat*cpReat       #Energia de F2
    eReat+=tEntr*fReat*cpReat       #Energia de F1

    eReat+=(tCam-tReat)*timeCam*coefG #Energia da camisa

    tReat=eReat/(cpReat*massReat)

    luck=random.randint(0,100)
    if luck<50:
        luck=random.randint(0,2)
        luck=luck*random.randint(-1,1)
        tReat+=luck
    elif luck<80:
        luck=random.randint(0,5)
        luck=luck*random.randint(-1,1)
        tReat+=luck
    elif luck<99:
        luck=random.randint(0,10)
        luck=luck*random.randint(-1,1)
        tReat+=luck
    else:
        luck=random.randint(0,15)
        luck=luck*random.randint(-1,1)
        tReat+=luck

    eReatIdeal=tIdeal*cpReat*massReat
    eReat=tReat*cpReat*massReat
    tCamOld=tCam

    tCam=tReat-((eReat-eReatIdeal)/(timeCam*coefG))    

    if abs(tCam-tCamOld)>limVar:
        if tCam>tCamOld:
            tCam=tCamOld+limVar
        else:
            tCam=tCamOld-limVar

    print(f'Loop {n}')
    print(f'Temperatura do Reator: {tReat}')
    print(f"Temperatura do fluido da camisa: {tCam}")
    tempsR.append(tReat)
    timeCounter.append(n)
    tempsC.append(tCam)

    if tReat>tCrit: 
        #messagebox.showwarning("Warning", "Temperature above critical!")
        failure+=1
    if tReat<tMin:
        #messagebox.showwarning("Warning", "Temperature below minimum!") '''
        failure+=1
    if n==3000 or n==6000 or n==9000 or n==12000:
        failureCounter.append(failure)
        failure=0
    time.sleep(0)
    if n==3000:
        limVar=10
    if n==6000:
        limVar=100
    if n==9000:
        limVar=100000    
    if n==12000:
        print(f'Falhas com variação da temperatura da camisa por segundo=0: {failureCounter[0]}')
        print(f'Falhas com variação de temperatura da camisa por segundo=10: {failureCounter[1]}')
        print(f'Falhas com variação de temperatura da camisa por segundo=100: {failureCounter[2]}')
        print(f'Falhas com variação de temperatura da camisa por segundo=ilimitado: {failureCounter[3]}')
        plt.figure(figsize=(8, 5))
        plt.plot(timeCounter, tempsR, marker='o',markersize=1, color='blue')
        #plt.plot(timeCounter, tempsC, linestyle='--',linewidth=1, color='red')
        plt.axhline(y=tCrit, color='green', linestyle='--', linewidth=1, label='Max Temperature')
        plt.axhline(y=tMin, color='green', linestyle='--', linewidth=1, label='Min Temperature')
        plt.axvline(x=3000, color='green', linestyle='-', linewidth=2, )
        plt.axvline(x=6000, color='green', linestyle='-', linewidth=2, )
        plt.axvline(x=9000, color='green', linestyle='-', linewidth=2, )
        plt.grid()
        plt.show()

    n+=1
