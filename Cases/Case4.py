import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dadosPrime = r'C:\Users\breno\Favorites\Downloads\Case4DataPrime - dados_experimentais.csv'

df=pd.read_csv(dadosPrime)

df = df.drop(columns=['dados aleatorios'])

df['Tempo'] = range(0, len(df))

df = df.dropna(subset=['Concentração (mol/L)'])
df = df.dropna(subset=['pH'])


plt.figure(1)
plt.figure(figsize=(10, 6))  # Optional: set the size of the plot
plt.plot(df['Tempo'], df['Concentração (mol/L)'], marker='o', linestyle='-')
plt.title('Tempo vs Concentração (mol/L)')
plt.xlabel('Tempo')
plt.ylabel('Concentração (mol/L)')
plt.ylim(0, 0.2)
plt.grid(True) 

def graphSet(xAxis, yAxis, upperLim, lowerLim, figNum):

    mediaGeral = df.groupby(xAxis)[yAxis].mean().reset_index()

    plt.figure(figNum)
    plt.figure(figsize=(10, 6)) 
    plt.plot(mediaGeral[xAxis], mediaGeral[yAxis], marker='o')
    plt.title(f'{xAxis} vs {yAxis}')
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)
    plt.ylim(lowerLim, upperLim)
    plt.grid(True)  

graphSet('pH','Concentração (mol/L)', 0.2,   0,   2)
graphSet('Temperatura (°C)','Concentração (mol/L)', 0.2,   0,   2)
graphSet('Temperatura (°C)','pH', 6,   8,   2)

ConcMedia = df['Concentração (mol/L)'].mean()

ConcMax=df['Concentração (mol/L)'].max()
ConcMin=df['Concentração (mol/L)'].min()

maxTempo = df.loc[df['Concentração (mol/L)'].idxmax(), 'Tempo']
minTempo = df.loc[df['Concentração (mol/L)'].idxmin(), 'Tempo']

variacaoMedia=df['Concentração (mol/L)'].diff().mean()
desvioPadrao=df['Concentração (mol/L)'].std()

print(f'Concentração média é {ConcMedia} mol/l')
print(f'Concentração máxima: {ConcMax} mol/l, ocorreu em {maxTempo} minutos')
print(f'Concentração mínima em {ConcMin} mol/l, ocorreu em {minTempo} minutos')

print()

print(f'Variação média da concentração é {variacaoMedia} e o desvio padrão é {desvioPadrao}')


plt.show()