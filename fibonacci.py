import random
import statistics
from matplotlib import pyplot
import numpy as np

#variables
capitalInicial = 0
def fCapital(x):
    return capitalInicial
def promGanadores(x):
    return (statistics.mean(ganadores))
def promPerdedores(x):
    return (statistics.mean(perdedores))
costo = 0
perdedores=[]
ganadores=[]

y=[]
apuesta = [37] #apuesta a realizar
valorApuestaB = [20] #valor base a apostar
balance=[]
posicionPerdida=[]
#colores del 0 al 36
#0: rojo
#1: negro
#2: ni rojo ni negro
#0 es par 1 es Impar
colores = [2,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0]
fibonacci=[0,1,1]
n=2

for rep in range(30):#cantidad de jugadores
    listaGanadas=[]
    ganadas = 0
    capital = capitalInicial
    i=0
    valorApuesta = []
    for s in range (0,len(valorApuestaB)):
        valorApuesta.insert(s,valorApuestaB[s])
    base = sum(valorApuestaB)
    costo=base
    capitalMomento=[capital]
    cantPer=0
    while (i<=1000):
        win=0
        capital = capital - costo
        y.insert(i, random.randint(0,36))
    
        colorG=colores[y[i]]


        if (y[i]%2)==0: 
            paridad=0 
        else: 
            paridad=1

        docena=0
        if (y[i]>=1 and y[i]<=12):
            docena=1
        elif(y[i]>=13 and y[i]<=24):
            docena=2
        elif(y[i]>=25 and y[i]<=36):
            docena=3

        columna=0
        if((y[i]%3)==0):
            columna=3
        elif(y[i]==2 or (y[i]%3)==2):
            columna=2
        elif(y[i]==1 or (y[i]%3)==1):
            columna=1
        mitad=0
        if (y[i]>=1 and y[i]<=18):
            mitad=1
        elif(y[i]>=19 and y[i]<=36):
            mitad=2

        for j in range (0, len(apuesta)):
        
            if (apuesta[j] >= 0 and apuesta[j] <= 36 and apuesta[j]==y[i]):
                capital = capital + (valorApuesta[apuesta.index(y[i])] * 36)
                win=1
            if (apuesta[j] == 37 and colorG==0):
                capital = capital + (valorApuesta[apuesta.index(37)] * 2)
                win=1
            if (apuesta[j] == 38 and colorG==1):
                capital = capital + (valorApuesta[apuesta.index(38)] * 2)
                win=1
            if (apuesta[j] == 39 and paridad==0):
                capital = capital + (valorApuesta[apuesta.index(39)] * 2)
                win=1
            if (apuesta[j] == 40 and paridad==1):
                capital = capital + (valorApuesta[apuesta.index(40)] * 2)
                win=1
            if (apuesta[j] == 41 and mitad==1):
                capital = capital + (valorApuesta[apuesta.index(41)] * 2)
                win=1
            if (apuesta[j] == 42 and mitad==2):
                capital = capital + (valorApuesta[apuesta.index(42)] * 2)
                win=1
            if (apuesta[j] == 43 and docena==1):
                capital = capital + (valorApuesta[apuesta.index(43)] * 3)
                win=1
            if (apuesta[j] == 44 and docena==2):
                capital = capital + (valorApuesta[apuesta.index(44)] * 3)
                win=1
            if (apuesta[j] == 45 and docena==3):
                capital = capital + (valorApuesta[apuesta.index(45)] * 3)
                win=1
            if (apuesta[j] == 46 and columna==1):
                capital = capital + (valorApuesta[apuesta.index(46)] * 3)
                win=1
            if (apuesta[j] == 47 and columna==2):
                capital = capital + (valorApuesta[apuesta.index(47)] * 3)
                win=1
            if (apuesta[j] == 48 and columna==3):
                capital = capital + (valorApuesta[apuesta.index(48)] * 3)
                win=1
                
        if (win==0):
            cantPer=cantPer+1
            if (len(fibonacci)==cantPer):
                fibonacci.append(fibonacci[n] + fibonacci[n-1])
                n=n+1
            costo = base * fibonacci[cantPer]
            for s in range (0,len(valorApuestaB)): 
                valorApuesta[s] = valorApuestaB[s] * fibonacci[cantPer]
        else:
            ganadas=ganadas+1
            if (cantPer<=2):
                cantPer=0
                costo = base * fibonacci[cantPer]
                for s in range (0,len(valorApuestaB)):
                    valorApuesta[s] = valorApuestaB[s] * fibonacci[cantPer]
            else:
                cantPer=cantPer-2
                costo = base*fibonacci[cantPer]
            for s in range (0,len(valorApuestaB)):
                valorApuesta[s] = valorApuestaB[s] * fibonacci[cantPer]

        if(fibonacci[cantPer]==0):
            costo=base
            for s in range (0,len(valorApuestaB)):
                valorApuesta[s] = valorApuestaB[s]
                
        if (capital <= costo):
            posicionPerdida.append(i)

        i=i+1
        listaGanadas.append(ganadas/(i))
        capitalMomento.insert(i,capital)
    
    balance.insert(0,capital-capitalInicial)

    x=np.arange(0,i+1,1)

    pyplot.figure('Evolucion del capital')
    pyplot.plot(x,capitalMomento, label=("flujo de caja",rep+1))
    pyplot.grid()
    pyplot.xlim(0, 1000)
    pyplot.xlabel('Tirada')
    pyplot.ylabel('Capital')
    pyplot.title('Evolucion del capital')
    pyplot.savefig('Evolucion del capital_Fibonacci_infi.png') 
    j=np.arange(0,len(listaGanadas),1)
    
    pyplot.figure('frsa')
    pyplot.plot(j,listaGanadas)
    pyplot.grid()
    pyplot.xlim(0,1000)
    pyplot.ylim(0,1)
    pyplot.xlabel('n (número de tiradas)')
    pyplot.ylabel('fr (frecuencia relativa)')
    pyplot.title('Frecuencia relativa de obtener la apuesta favorable según n')
    pyplot.savefig('frsa_Fibonacci_infi.png')
pyplot.plot(x,[fCapital(i) for i in x], label="flujo de caja inicial")


p=np.arange(0,rep+1,1)
pyplot.figure('Balance')
pyplot.scatter(p,balance)
pyplot.grid()
pyplot.xlim(0, rep)
pyplot.xlabel('Jugador')
pyplot.ylabel('Balance')
pyplot.title('Balance por Jugador')
pyplot.savefig("Balance por Jugador_Fibonacci_infi.png")
for i in range (0,rep):
    if(balance[i]<0):
        perdedores.append(balance[i])
    if(balance[i]>=0):
        ganadores.append(balance[i])

pyplot.figure('Promedio ganadores')
x=np.arange(0,100,1)
pyplot.plot(x,[promGanadores(i) for i in x], label="balance final promedio de ganadores")
pyplot.grid()
pyplot.ylabel('Balance')

pyplot.figure('Promedio perdedores')
x=np.arange(0,100,1)
pyplot.plot(x,[promPerdedores(i) for i in x], label="balance final promedio de perdedores")
pyplot.grid()
pyplot.ylabel('Balance')
print(posicionPerdida)
print(statistics.mean(posicionPerdida))
pyplot.legend(loc='lower left')
pyplot.show()

