import random
import statistics
from matplotlib import pyplot
import numpy as np

#0-36 → x36
#37 apuesta al rojo →x2
#38 apuesta al negro → x2
#39 apuesta par → x2
#40 apuesta impar → x2
#41 apuesta a la falta (1 - 18) →x2
#42 apuesta a la pasa (19 -36) → x2
#43 apuesta al primer docena → x3
#44 apuesta a la segunda docena → x3
#45 apuesta a la tercer docena → x3
#46 apuesta a la primer columna → x3
#47 apuesta a la segunda columna → x3
#48 apuesta a la tercer columna → x3

#variables
capitalInicio=0
capital = capitalInicio
costo = 0

i = 0
y=[]
posicionPerdida=[]
apuesta = [37]
valorApuestaB = [20]
valorApuesta = []
for s in range (0,len(valorApuestaB)):
   valorApuesta.insert(s,valorApuestaB[s])
base = sum(valorApuestaB)
#costo=base
#capitalMomento=[capital]
perdedores=[]
ganadores=[]
balance=[]
#colores del 0 al 36
#0: rojo
#1: negro
#2: ni rojo ni negro
#0 es par 1 es Impar
colores = [2,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0]

for k in range(30):
    capital = capitalInicio   
    costo=base
    listaGanadas=[]
    ganadas = 0
    capitalMomento=[capital] 
    i=0
    for w in range (0,len(valorApuestaB)):
        valorApuesta.insert(w,valorApuestaB[w])
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
            costo = costo * 2
            for s in range (0,len(valorApuestaB)):
                    valorApuesta[s] = valorApuesta[s] * 2
        else:   
            ganadas=ganadas+1
            costo = base
            for s in range (0,len(valorApuestaB)):
                valorApuesta[s] = valorApuestaB[s]
        
        if (capital <= costo):
            posicionPerdida.append(i)
        
        i=i+1
        capitalMomento.insert(i,capital)
        listaGanadas.append(ganadas/(i))

    
    balance.insert(k, capital-capitalInicio)   
    if (balance[k]>=0):
        ganadores.append(balance[k])
    else:
        perdedores.append(balance[k])

    x=np.arange(0,i+1,1)

    #Frec Relativa
    pyplot.figure('Evolucion del capital')
    pyplot.plot(x,capitalMomento)
    pyplot.grid()
    pyplot.xlim(0, 1000)
    pyplot.xlabel('Tirada')
    pyplot.ylabel('Capital')
    pyplot.title('Evolucion del capital')  
    pyplot.savefig('Evolucion del capital_MartinGala_Infi.png') 
    j=np.arange(0,len(listaGanadas),1)
    
    pyplot.figure('frsa')
    pyplot.plot(j,listaGanadas)
    pyplot.grid()
    pyplot.xlim(0,1000)
    pyplot.ylim(0,1)
    pyplot.xlabel('n (número de tiradas)')
    pyplot.ylabel('fr (frecuencia relativa)')
    pyplot.title('Frecuencia relativa de obtener la apuesta favorable según n')
    pyplot.savefig('frsa_MartinGala_Infi.png')



p=np.arange(0,k+1,1)
pyplot.figure('Balance')
pyplot.scatter(p,balance)
pyplot.grid()
pyplot.xlim(0, k)
pyplot.xlabel('Jugador')
pyplot.ylabel('Balance')
pyplot.title('Balance por Jugador')  
pyplot.savefig("Balance por Jugador_MartinGala_Infi.png")
#def promper(x):
#    return statistics.mean(perdedores)

def promgan(x):
    return statistics.mean(ganadores)
pyplot.figure('Promedio ganadores')
x=np.arange(0,1000,1)
pyplot.plot(x,[promgan(i) for i in x], label="balance final promedio de ganadores")
pyplot.grid()
pyplot.ylabel('Balance')
#pyplot.savefig("Promedio ganadores_MartinGala.jpg")


#pyplot.figure('Promedio perdedores')
#x=np.arange(0,1000,1)
#pyplot.plot(x,[promper(i) for i in x], label="balance final promedio de perdedores")
#pyplot.grid()
#pyplot.ylabel('Balance')
print(posicionPerdida)
print(statistics.mean(posicionPerdida))
print (str(balance))
print(str(capitalMomento))
print(str(perdedores))
print(str(ganadores))
print(str (listaGanadas))




#pyplot.savefig("Promedio perdedores_MartinGala.jpg")

pyplot.show()