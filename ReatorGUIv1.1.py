import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import math 
import numpy as np
import random
import time
import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class ScrollableWindow(QtWidgets.QMainWindow):
    def __init__(self, fig):
        self.qapp = QtWidgets.QApplication([])

        QtWidgets.QMainWindow.__init__(self)
        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0,0,0,0)
        self.widget.layout().setSpacing(0)

        self.fig = fig
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QtWidgets.QScrollArea(self.widget)
        self.scroll.setWidget(self.canvas)

        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.scroll)

        self.show()
        exit(self.qapp.exec_()) 





def start_program():
    try:
        # Collect the input values from the Entry widgets
        global CLIprog
        global camLims
        global fReat
        global pertInt
        global concsIn
        global concsInit
        global lenOfTest
        global massReat
        global cooldownBase
        global resolution
        global progBar

        pertInt = float(entry_pertInt.get())
        camLims = [
            float(entry_camLims0.get()),  # Placeholder for index alignment (camLims[0] unused)
            float(entry_camLims1.get()),
            float(entry_camLims2.get()),
            float(entry_camLims3.get())
        ]

        concsIn=[
            float(entry_concsInA.get()),
            0,
            float(entry_concsInC.get()),
            0
        ]

        concsInit=[
            float(entry_concsInitA.get()),
            float(entry_concsInitB.get()),
            float(entry_concsInitC.get()),
            float(entry_concsInitD.get())
        ]


        fReat = float(entry_fReat.get())
        lenOfTest=int(entry_lenOfTest.get())
        massReat=int(entry_massReat.get())
        cooldownBase=int(entry_cooldownBase.get())
        resolution=float(entry_resolution.get())

        progBar = var_progBar.get()
        CLIprog = var_CLIprog.get()

        root.destroy()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Reactor Parameter Input")

# Labels and Entry widgets for each parameter
tk.Label(root, text="Set the perturbation intensity:").grid(row=0, column=0, padx=10, pady=5)
entry_pertInt = tk.Entry(root, textvariable=tk.StringVar(value="1"))
entry_pertInt.grid(row=0, column=1)

tk.Label(root, text="First cooling shirt limit:").grid(row=1, column=0, padx=10, pady=5)
entry_camLims0 = tk.Entry(root, textvariable=tk.StringVar(value="0"))
entry_camLims0.grid(row=1, column=1)

tk.Label(root, text="Second cooling shirt limit:").grid(row=2, column=0, padx=10, pady=5)
entry_camLims1 = tk.Entry(root, textvariable=tk.StringVar(value="10"))
entry_camLims1.grid(row=2, column=1)

tk.Label(root, text="Third cooling shirt limit:").grid(row=3, column=0, padx=10, pady=5)
entry_camLims2 = tk.Entry(root, textvariable=tk.StringVar(value="20"))
entry_camLims2.grid(row=3, column=1)

tk.Label(root, text="Fourth cooling shirt limit:").grid(row=4, column=0, padx=10, pady=5)
entry_camLims3 = tk.Entry(root, textvariable=tk.StringVar(value="40"))
entry_camLims3.grid(row=4, column=1)

tk.Label(root, text="Set the reactor flow (kg/s):").grid(row=5, column=0, padx=10, pady=5)
entry_fReat = tk.Entry(root, textvariable=tk.StringVar(value="1"))
entry_fReat.grid(row=5, column=1)

tk.Label(root, text="Set A flow concentration (mol/kg):").grid(row=6, column=0, padx=10, pady=5)
entry_concsInA = tk.Entry(root, textvariable=tk.StringVar(value="2"))
entry_concsInA.grid(row=6, column=1)

tk.Label(root, text="Set C flow concentration (mol/kg):").grid(row=7, column=0, padx=10, pady=5)
entry_concsInC = tk.Entry(root, textvariable=tk.StringVar(value="2"))
entry_concsInC.grid(row=7, column=1)

tk.Label(root, text="Set resolution(s^-1):").grid(row=8, column=0, padx=10, pady=5)
entry_resolution = tk.Entry(root, textvariable=tk.StringVar(value="1"))
entry_resolution.grid(row=8, column=1)

tk.Label(root, text="Set initial A concentration (mol/kg):").grid(row=0, column=2, padx=10, pady=5)
entry_concsInitA = tk.Entry(root, textvariable=tk.StringVar(value="0.1"))
entry_concsInitA.grid(row=0, column=3)

tk.Label(root, text="Set initial B concentration (mol/kg):").grid(row=1, column=2, padx=10, pady=5)
entry_concsInitB = tk.Entry(root, textvariable=tk.StringVar(value="0.1"))
entry_concsInitB.grid(row=1, column=3)

tk.Label(root, text="Set initial C concentration (mol/kg):").grid(row=2, column=2, padx=10, pady=5)
entry_concsInitC = tk.Entry(root, textvariable=tk.StringVar(value="0.1"))
entry_concsInitC.grid(row=2, column=3)

tk.Label(root, text="Set initial D concentration (mol/kg):").grid(row=3, column=2, padx=10, pady=5)
entry_concsInitD = tk.Entry(root, textvariable=tk.StringVar(value="1.9"))
entry_concsInitD.grid(row=3, column=3)

tk.Label(root, text="Set lenght of cycle:").grid(row=4, column=2, padx=10, pady=5)
entry_lenOfTest = tk.Entry(root, textvariable=tk.StringVar(value="30000"))
entry_lenOfTest.grid(row=4, column=3)

tk.Label(root, text="Set mass capacity of the reactor (kg):").grid(row=5, column=2, padx=10, pady=5)
entry_massReat = tk.Entry(root, textvariable=tk.StringVar(value="10000"))
entry_massReat.grid(row=5, column=3)

tk.Label(root, text="Set lenght of cooldown (s):").grid(row=6, column=2, padx=10, pady=5)
entry_cooldownBase = tk.Entry(root, textvariable=tk.StringVar(value="10"))
entry_cooldownBase.grid(row=6, column=3)

var_progBar = tk.BooleanVar()
progBar_checkbox = tk.Checkbutton(root, text="Enable GUI progress bar", variable=var_progBar)
progBar_checkbox.grid(row=7, column=2, columnspan=2, pady=5)


var_CLIprog = tk.BooleanVar()
CLIprog_checkbox = tk.Checkbutton(root, text="Enable CLI progress bar", variable=var_CLIprog)
CLIprog_checkbox.grid(row=8, column=2, columnspan=2, pady=5)


# Start Button to trigger the main code
start_button = tk.Button(root, text="Start", command=start_program)
start_button.grid(row=9, column=1, columnspan=2, pady=10)


# Run the Tkinter event loop
root.mainloop()



tIdeal=308 # temperatura ideal        unidade = Kelvin
tCrit=313 # temperatura crítica       unidade = Kelvin 
tEntr=300 # temperatura de entrada    unidade = Kelvin
tReat=300 # temperatura do reator     unidade = Kelvin
tCam=308 # temperatura da camisa      unidade = Kelvin
tMin=290 # temperatura mínima         unidade = Kelvin


# Reação A->B
#  C+B-> D (produto final)
constA=0.03
constD=0.02
concsReat=concsInit.copy()



fCam=50    # vazão da camisa                   unidade = kg/s
coefG=50000    #coeficiente global                unidade = W/K
cpCam=50   # calor específico da camisa        unidade = j/(Kg * K)
cpReat=150 # calor específico do reator        unidade = j/(Kg * K)

dtime=resolution**-1 #Resolução é o inverso do time step de cada ciclo
lenOfTest=int(lenOfTest*resolution)

limVar=camLims[0] #Limite do quanto a temperatura da camisa consegue variar em 1 segundo
tCamOld=tCam

failure=0


timeCounter=[]
tempsR=[]
tempsC=[]
effs=[]
ReacRates=[[],[]]
concsFinal=[[],[],[],[]]
failureCounter=[]

cooldownBase=cooldownBase*resolution
cooldown=0
cooldownCounter=[]

startTimer = time.perf_counter()

if progBar:
    prog = tk.Tk()
    prog.title("Loading results...")
                                                    #set up progress bar
    progress_bar = ttk.Progressbar(prog, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=20)

    progress_label = tk.Label(prog, text="0% Complete")
    progress_label.pack()

for n in range(lenOfTest*4+1):

    for subst in range(0,4):
        concsReat[subst]+=((-concsReat[subst]*fReat+concsIn[subst]*fReat)/massReat) * dtime   #Variação da 
                                                                                #concentração pelos fluxos de 
                                                                                #entrada e saída
                

     #Eficiência da reação, Bell curve centrada em 308

    if cooldown!=0:
        cooldown-=1
        eff=0
        failure+=1
        cooldownCounter.append(2)
    else:
        eff=np.exp(-((tReat - 308) ** 2) / (2 * 2 ** 2))
        cooldownCounter.append(None)

    ReacRateA=((concsReat[0])**2)*constA*eff* dtime     #Cálculo da taxa reacional
    ReacRateD=concsReat[1]*concsReat[2]*constD*eff * dtime


    concsReat[0]+=-ReacRateA
    concsReat[1]+=ReacRateA - ReacRateD
    concsReat[2]+=-ReacRateD         #Variação da concentração por reação
    concsReat[3]+=ReacRateD
    
    eReat=tReat*cpReat*massReat     #Energia dentro do reator
    eReat-=tReat*fReat*cpReat*dtime       #Energia de F2
    eReat+=tEntr*fReat*cpReat*dtime       #Energia de F1

    eReat+=(tCam-tReat)*coefG*dtime #Energia da camisa

    eReat+=ReacRateA*massReat*50000 #Energia da primeira reação
    eReat+=ReacRateD*massReat*70000   #Energia da segunda reação

    tReat=eReat/(cpReat*massReat)

    tReat+=np.random.normal(loc=0, scale=pertInt)*dtime    #Perturbação
    
    eReatIdeal=tIdeal*cpReat*massReat
    eReat=tReat*cpReat*massReat             #cálculo das entalpias e preparação para o cálculo da camisa
    tCamOld=tCam

    tCam=tReat-((eReat-eReatIdeal)/(coefG))*dtime

    if abs(tCam-tCamOld)>limVar:
        if tCam>tCamOld:
            tCam=tCamOld+limVar*dtime                       #limitador da variação da camisa
        else:
            tCam=tCamOld-limVar*dtime

    if ((n/(lenOfTest*4))*100)%1==0:

        if progBar:
            progress_percent = (n * 100) / (lenOfTest * 4)
            progress_bar["value"] = progress_percent                #GUI progress bar
            progress_label.config(text=f"{progress_percent:.2f}% Complete")
            prog.update_idletasks()
        if CLIprog:    
            print(f'{n*100/(lenOfTest*4):.2f}%')                    #CLI loading bar
    
    
    tempsR.append(tReat)
    timeCounter.append(n*dtime)
    tempsC.append(tCam)
    effs.append(eff)                    #appending results to the graphs
    ReacRates[0].append(ReacRateA)
    ReacRates[1].append(ReacRateD)

    for i in range(0,4):
        concsFinal[i].append(concsReat[i])
    
    if tReat>tCrit: 
        #messagebox.showwarning("Warning", "Temperature above critical!")
        cooldown=cooldownBase
    if tReat<tMin:
        #messagebox.showwarning("Warning", "Temperature below minimum!") '''
        cooldown=cooldownBase
    if n==lenOfTest or n==lenOfTest*2 or n==lenOfTest*3 or n==lenOfTest*4:
        failureCounter.append(failure)
        failure=0
    #time.sleep(0)
    if n==lenOfTest:
        limVar=camLims[1]
    if n==lenOfTest*2:
        limVar=camLims[2]
    if n==lenOfTest*3:
        limVar=camLims[3]    
    if n==lenOfTest*4:
                
        vazMed=[0,0,0,0]
        for m in range(0,4):
            for i in range(m*lenOfTest,(m+1)*lenOfTest):
                vazMed[m]+=concsFinal[3][i]
            vazMed[m]=vazMed[m]/lenOfTest                           #Calculando a vazão média de cada bloco
            vazMed[m]=vazMed[m]*fReat
        for i in range (0,4):
            print(f'Falhas com variação da temperatura da camisa por segundo={camLims[i]}: {failureCounter[i]}')
            print(f'Vazão de produto com variação da temperatura da camisa por segundo={camLims[i]}: {vazMed[i]} mol/s')

        effsReduced=[]
        for i in range(len(effs)):
            if i%150==0:
                effsReduced.append(sum(effs[i:i+(int(150*resolution)-1)])/ (150*resolution))         #Fazendo eficiência ser legível
            else:
                effsReduced.append(None)

        ReacRatesReduced=[[],[]]
        for i in range(len(ReacRates[0])):
            if i%150==0:
                ReacRatesReduced[0].append(sum(ReacRates[0][i:i+(int(150*resolution)-1)])/ (150*resolution))         #Fazendo eficiência ser legível
            else:
                ReacRatesReduced[0].append(None)
        
        for i in range(len(ReacRates[1])):
            if i%150==0:
                ReacRatesReduced[1].append(sum(ReacRates[1][i:i+(int(150*resolution)-1)])/ (150*resolution))         #Fazendo eficiência ser legível
            else:
                ReacRatesReduced[1].append(None)

        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        axes = axes.flatten()

        axes[0].plot(timeCounter, tempsR, marker='o',markersize=1, color='blue')
        #axes[0].plot(timeCounter, tempsC, marker='o',markersize=1, color='red')
        axes[0].set_title('Temperature profile')
        axes[0].axhline(y=tCrit, color='green', linestyle='--', linewidth=1, label='Max Temperature')
        axes[0].axhline(y=tMin, color='green', linestyle='--', linewidth=1, label='Min Temperature')
        axes[0].axvline(x=lenOfTest, color='green', linestyle='-', linewidth=1, )
        axes[0].axvline(x=lenOfTest*2, color='green', linestyle='-', linewidth=1, )
        axes[0].axvline(x=lenOfTest*3, color='green', linestyle='-', linewidth=1, )
        axes[0].grid
        axes[0].legend(loc='best')

        axes[1].set_title('Concentration in the reactor and out flow')
        axes[1].scatter(timeCounter, cooldownCounter, s=1, color='purple', label="Cooldown")
        axes[1].plot(timeCounter, concsFinal[0], marker='o',markersize=1, color='blue', label="A")
        axes[1].plot(timeCounter, concsFinal[1], marker='o',markersize=1, color='green', label="B")
        axes[1].plot(timeCounter, concsFinal[2], marker='o',markersize=1, color='red',label="C")
        axes[1].plot(timeCounter, concsFinal[3], marker='o',markersize=1, color='pink', label="D")
        axes[1].axvline(x=lenOfTest*dtime, color='green', linestyle='-', linewidth=1, )
        axes[1].axvline(x=lenOfTest*2*dtime, color='green', linestyle='-', linewidth=1, )
        axes[1].axvline(x=lenOfTest*3*dtime, color='green', linestyle='-', linewidth=1, )
        axes[1].legend(loc='best')

        axes[2].set_title('Efficiency')
        axes[2].scatter(timeCounter, effs, s=2, color='orange')
        axes[2].scatter(timeCounter, effsReduced, s=2, color='purple')
        axes[2].axvline(x=lenOfTest*dtime, color='green', linestyle='-', linewidth=1, )
        axes[2].axvline(x=lenOfTest*2*dtime, color='green', linestyle='-', linewidth=1, )
        axes[2].axvline(x=lenOfTest*3*dtime, color='green', linestyle='-', linewidth=1, )

        axes[3].set_title('Reaction Rates')
        axes[3].scatter(timeCounter, ReacRatesReduced[0], s=2, color='orange', label='Reaction Rate A')
        axes[3].scatter(timeCounter, ReacRatesReduced[1], s=2, color='purple', label='Reaction Rate D')
        axes[3].axvline(x=lenOfTest*dtime, color='green', linestyle='-', linewidth=1, )
        axes[3].axvline(x=lenOfTest*2*dtime, color='green', linestyle='-', linewidth=1, )
        axes[3].axvline(x=lenOfTest*3*dtime, color='green', linestyle='-', linewidth=1, )

        fig.text(0.5, 0.02, f'''Molar flow of D with no control= {vazMed[0]:.4f} mol/s | Conversion rate of A into D of {(vazMed[0]/(fReat*concsIn[0]))*100:.4f}%| Time spent in cooldown = {100*(failureCounter[0]/lenOfTest):.4f}%\n 
                 Molar flow of D with variance limit at {camLims[1]}= {vazMed[1]:.4f} mol/s | Conversion rate of A into D of {(vazMed[1]/(fReat*concsIn[0]))*100:.4f}%| Time spent in cooldown = {100*(failureCounter[1]/lenOfTest):.4f}% \n
                 Molar flow of D with variance limit at {camLims[2]}= {vazMed[2]:.4f} mol/s | Conversion rate of A into D of {(vazMed[2]/(fReat*concsIn[0]))*100:.4f}%| Time spent in cooldown = {100*(failureCounter[2]/lenOfTest):.4f}%\n
                 Molar flow of D with variance limit at {camLims[3]}= {vazMed[3]:.4f} mol/s | Conversion rate of A into D of {(vazMed[3]/(fReat*concsIn[0]))*100:.4f}%| Time spent in cooldown = {100*(failureCounter[3]/lenOfTest):.4f}%\n
                 Lenght of cycles = {lenOfTest} | Cooling limits in order: {camLims[0]}K /{camLims[1]}K /{camLims[2]}K /{camLims[3]}K | Perturbation intensity at {pertInt} \n
                 Initial concentration: [A]={concsInit[0]:.2f}mol/kg / [B]={concsInit[1]:.2f}mol/kg / [C]={concsInit[2]:.2f}mol/kg / [D]={concsInit[3]:.2f}mol/kg\n
                 Massa do reator={massReat}kg | Vazão das correntes do reator ={fReat}kg/s\n 
                 Concentrações de entrada: [A]={concsIn[0]:.2f}mol/kg / [B]={concsIn[1]:.2f}mol/kg / [C]={concsIn[2]:.2f}mol/kg / [D]={concsIn[3]:.2f}mol/kg''',
         wrap=True, horizontalalignment='center', fontsize=10)
        fig.subplots_adjust(bottom=0.3)

        plt.grid()

        if progBar:
            prog.destroy()

        endTimer = time.perf_counter()
        print(f'Time elapse= {endTimer-startTimer:.2f} seconds')
        a = ScrollableWindow(fig)
        plt.show()
        sys.exit()
