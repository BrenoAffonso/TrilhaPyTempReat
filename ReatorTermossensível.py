import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
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
medianGain=0

massReat=10000  # massa do reator     unidade = kg

root = tk.Tk()
root.title("Temperature Warning")
n=1


timeCounter=[]
tempsR=[]
tempsC=[]
failureCounter=[]
gainCounter=[]

GreaterLoopCounterlist=[0]

critFailure=False

noFwdFeedFailure=[0,0,0,0]
noFwdFeedGain=[0,0,0,0]

generalCyclesCounter=0

GreaterLoopCounter=0
while GreaterLoopCounter<50:
    n=0
    while n!=12001:
        generalCyclesCounter+=1
        eReat=tReat*cpReat*massReat     #Energia dentro do reator
        eReat-=tReat*fReat*cpReat       #Energia de F2
        eReat+=tEntr*fReat*cpReat       #Energia de F1

        eReat+=(tCam-tReat)*timeCam*coefG #Energia da camisa
        
        if not critFailure:
            eReat+=500000* np.exp(-((tReat - 308) ** 2) / (2 * 5.75 ** 2))
            medianGain+=500000* np.exp(-((tReat - 308) ** 2) / (2 * 5.75 ** 2))    #Energia da reação(exotérmica)
        else:
            critTimeout-=1
            failure+=1
            print("FAILURE")
            if critTimeout==0:
                critFailure=False                                        #Timeout for above critical



        tReat=eReat/(cpReat*massReat)  

        luck=random.randint(0,100)
        if luck<50:
            luck=random.randint(0,1)
            luck=luck*random.randint(-1,1)       #sistema de pertubações
            tReat+=luck
        elif luck<80:
            luck=random.randint(0,2)
            luck=luck*random.randint(-1,1)
            tReat+=luck
        elif luck<99:
            luck=random.randint(0,3)
            luck=luck*random.randint(-1,1)
            tReat+=luck
        else:
            luck=random.randint(0,5)
            luck=luck*random.randint(-1,1)
            tReat+=luck

        if tReat>313 or tReat<290:
            print("Failure")
            critFailure=True
            critTimeout=10

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

        #if tReat>tCrit: 
            #messagebox.showwarning("Warning", "Temperature above critical!")
        #if tReat<tMin:
            #messagebox.showwarning("Warning", "Temperature below minimum!") '''

        if n==3000 or n==6000 or n==9000 or n==12000:
            gainCounter.append(medianGain/3000)
            medianGain=0
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
            noFwdFeedFailure[0]+=failureCounter[0]

            noFwdFeedFailure[1]+=failureCounter[1]
            noFwdFeedFailure[2]+=failureCounter[2]
            noFwdFeedFailure[3]+=failureCounter[3]


            print(f'Ganho com variação da temperatura da camisa por segundo=0: {gainCounter[0]}')
            print(f'Ganho com variação de temperatura da camisa por segundo=10: {gainCounter[1]}')
            print(f'Ganhp com variação de temperatura da camisa por segundo=100: {gainCounter[2]}')
            print(f'Ganho com variação de temperatura da camisa por segundo=ilimitado: {gainCounter[3]}')
            noFwdFeedGain[0]+=gainCounter[0]
            noFwdFeedGain[1]+=gainCounter[1]
            noFwdFeedGain[2]+=gainCounter[2]
            noFwdFeedGain[3]+=gainCounter[3]


            plt.figure(figsize=(8, 5))
            plt.plot(timeCounter, tempsR, marker='o',markersize=1, color='blue')
            #plt.plot(timeCounter, tempsC, linestyle='--',linewidth=1, color='red')
            plt.axhline(y=tCrit, color='green', linestyle='--', linewidth=1, label='Max Temperature')
            plt.axhline(y=tMin, color='green', linestyle='--', linewidth=1, label='Min Temperature')
            plt.axvline(x=3000, color='green', linestyle='-', linewidth=2, )
            plt.axvline(x=6000, color='green', linestyle='-', linewidth=2, )
            plt.axvline(x=9000, color='green', linestyle='-', linewidth=2, )
            plt.grid()
            #plt.show()
        n+=1
    GreaterLoopCounter+=1
    GreaterLoopCounterlist[0]+=1



timeCounter=[]
tempsR=[]
tempsC=[]
failureCounter=[]
gainCounter=[]
failure=0
medianGain=0
n=0
limVar=0
tCam=308
tCamOld=308

wtFwdFeedFailure=[0,0,0,0]
wtFwdFeedGain=[0,0,0,0]

critFailure=False

GreaterLoopCounter=0
while GreaterLoopCounter<50:
    n=0
    while n!=12001:
        generalCyclesCounter+=1
        eReat=tReat*cpReat*massReat     #Energia dentro do reator
        eReat-=tReat*fReat*cpReat       #Energia de F2
        eReat+=tEntr*fReat*cpReat       #Energia de F1

        eReat+=(tCam-tReat)*timeCam*coefG #Energia da camisa
        
        if not critFailure:
            eReat+=500000* np.exp(-((tReat - 308) ** 2) / (2 * 5.75 ** 2))
            medianGain+=500000* np.exp(-((tReat - 308) ** 2) / (2 * 5.75 ** 2))    #Energia da reação(exotérmica)
        else:
            critTimeout-=1
            failure+=1
            print("FAILURE")
            if critTimeout==0:
                critFailure=False                                        #Timeout for above critical


        tReat=eReat/(cpReat*massReat)  

        luck=random.randint(0,100)
        if luck<50:
            luck=random.randint(0,1)
            luck=luck*random.randint(-1,1)       #sistema de pertubações
            tReat+=luck
        elif luck<80:
            luck=random.randint(0,2)
            luck=luck*random.randint(-1,1)
            tReat+=luck
        elif luck<99:
            luck=random.randint(0,3)
            luck=luck*random.randint(-1,1)
            tReat+=luck
        else:
            luck=random.randint(0,5)
            luck=luck*random.randint(-1,1)
            tReat+=luck

        if tReat>313 or tReat<290:
            print("Failure")
            critFailure=True
            critTimeout=10

        eReatIdeal=tIdeal*cpReat*massReat
        eReat=tReat*cpReat*massReat
        tCamOld=tCam

        tCam=tReat-((eReat-eReatIdeal)/(timeCam*coefG))-((500000* np.exp(-((tReat - 308) ** 2) / (2 * 5.75 ** 2)))/(timeCam*coefG))

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

        #if tReat>tCrit: 
            #messagebox.showwarning("Warning", "Temperature above critical!")
        #if tReat<tMin:
            #messagebox.showwarning("Warning", "Temperature below minimum!") '''

        if n==3000 or n==6000 or n==9000 or n==12000:
            gainCounter.append(medianGain/3000)
            medianGain=0
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
            wtFwdFeedFailure[0]+=failureCounter[0]
            wtFwdFeedFailure[1]+=failureCounter[1]
            wtFwdFeedFailure[2]+=failureCounter[2]
            wtFwdFeedFailure[3]+=failureCounter[3]

            print(f'Ganho com variação da temperatura da camisa por segundo=0: {gainCounter[0]}')
            print(f'Ganho com variação de temperatura da camisa por segundo=10: {gainCounter[1]}')
            print(f'Ganhp com variação de temperatura da camisa por segundo=100: {gainCounter[2]}')
            print(f'Ganho com variação de temperatura da camisa por segundo=ilimitado: {gainCounter[3]}')
            wtFwdFeedGain[0]+=gainCounter[0]
            wtFwdFeedGain[1]+=gainCounter[1]
            wtFwdFeedGain[2]+=gainCounter[2]
            wtFwdFeedGain[3]+=gainCounter[3]

            plt.figure(figsize=(8, 5))
            plt.plot(timeCounter, tempsR, marker='o',markersize=1, color='blue')
            #plt.plot(timeCounter, tempsC, linestyle='--',linewidth=1, color='red')
            plt.axhline(y=tCrit, color='green', linestyle='--', linewidth=1, label='Max Temperature')
            plt.axhline(y=tMin, color='green', linestyle='--', linewidth=1, label='Min Temperature')
            plt.axvline(x=3000, color='green', linestyle='-', linewidth=2, )
            plt.axvline(x=6000, color='green', linestyle='-', linewidth=2, )
            plt.axvline(x=9000, color='green', linestyle='-', linewidth=2, )
            plt.grid()
            #plt.show()
        n+=1
    GreaterLoopCounter+=1


print(f'noFwdFeedFailure at limVar=0: {noFwdFeedFailure[0]}')
print(f'noFwdFeedFailure at limVar=10: {noFwdFeedFailure[1]}')
print(f'noFwdFeedFailure at limVar=100: {noFwdFeedFailure[2]}')
print(f'noFwdFeedFailure at limVar=ilimitado: {noFwdFeedFailure[3]}')

print(f'wtFwdFeedFailure at limVar=0: {wtFwdFeedFailure[0]}')
print(f'wtFwdFeedFailure at limVar=10: {wtFwdFeedFailure[1]}')
print(f'wtFwdFeedFailure at limVar=100: {wtFwdFeedFailure[2]}')
print(f'wtFwdFeedFailure at limVar=ilimitado: {wtFwdFeedFailure[3]}')

print(f'noFwdFeedGain at limVar=0: {noFwdFeedGain[0]}')
print(f'noFwdFeedGain at limVar=10: {noFwdFeedGain[1]}')
print(f'noFwdFeedGain at limVar=100: {noFwdFeedGain[2]}')
print(f'noFwdFeedGain at limVar=ilimitado: {noFwdFeedGain[3]}')

print(f'wtFwdFeedGain at limVar=0: {wtFwdFeedGain[0]}')
print(f'wtFwdFeedGain at limVar=10: {wtFwdFeedGain[1]}')
print(f'wtFwdFeedGain at limVar=100: {wtFwdFeedGain[2]}')
print(f'wtFwdFeedGain at limVar=ilimitado: {wtFwdFeedGain[3]}')

FailureImprov=[]

FailureImprov.append(100*(wtFwdFeedFailure[0]/noFwdFeedFailure[0]))
FailureImprov.append(100*(wtFwdFeedFailure[1]/noFwdFeedFailure[1]))
FailureImprov.append(100*(wtFwdFeedFailure[2]/noFwdFeedFailure[2]))
FailureImprov.append(100*(wtFwdFeedFailure[3]/noFwdFeedFailure[3]))

GainImprov=[]

GainImprov.append(100*(wtFwdFeedGain[0]/noFwdFeedGain[0]))
GainImprov.append(100*(wtFwdFeedGain[1]/noFwdFeedGain[1]))
GainImprov.append(100*(wtFwdFeedGain[2]/noFwdFeedGain[2]))
GainImprov.append(100*(wtFwdFeedGain[3]/noFwdFeedGain[3]))
print()
print(f'Melhoria de falha em limVar=0: {FailureImprov[0]}%')
print(f'Melhoria de falha em limVar=10: {FailureImprov[1]}%')
print(f'Melhoria de falha em limVar=100: {FailureImprov[2]}%')
print(f'Melhoria de falha em limVar=ilimitado: {FailureImprov[3]}%')
print()
print(f'Melhoria de ganho em limVar=0: {GainImprov[0]}%')
print(f'Melhoria de ganho em limVar=10: {GainImprov[1]}%')
print(f'Melhoria de ganho em limVar=100: {GainImprov[2]}%')
print(f'Melhoria de ganho em limVar=ilimitado: {GainImprov[3]}%')


print (f'{generalCyclesCounter}')