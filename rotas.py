import requests
import numpy as np
import random as rd
from getCitizens import capitais_estaduais, index

## inicialização das matrizes e variáveis utilizadas no algorítmo
pops = np.load("pops.npy")
totalPops=np.sum(pops)
fileDis = np.load("popPerDist.npy", allow_pickle=True)
dis = fileDis.item(0)
feromonio = {}
cidIndex = list(index.keys())
for i in capitais_estaduais:
    aux = np.zeros(27)
    aux[index[i]] = 1 * 27
    feromonio[i] = np.ones(27)*27 - aux

for i in dis:
    dis[i][dis[i]>1600000] = 0

def initializer():
    NUMOFITER = int(input("Max Number of Iterations: "))
    NUMOFANTS = int(input("Number of ants to simulate: "))
    print(index)
    STARTCITY = cidIndex[int(input("Select starting city: "))]
    TAXAEVAP = float(input("taxa de evaporação: "))
    FERMONTOTAL = 27*27-27
    colonia = []
    for ants in range(NUMOFANTS):
        colonia.append(ANTS(STARTCITY))
    return NUMOFITER, NUMOFANTS, STARTCITY, FERMONTOTAL,TAXAEVAP, colonia

class ANTS:
    def __init__(self, initialLoc):
        self.caminho = [initialLoc]
        self.pops = pops[index[initialLoc]]

    def calcularCaminho(self):
        self.totalPops = self.pops
        self.percentPops = 0
        self.dist = 0
        self.popsDist = 0
        self.popsDistPercent = 0
        self.sumOfFer = 0 
        self.citiesVisited = 1


        while True:
            lugar = self.caminho[-1]
            localFer=feromonio[lugar].copy()
            for i in range(len(localFer)):
                if cidIndex[i] in self.caminho:
                    localFer[i] = 0
            atratividade = np.divide(pops+self.totalPops, self.dist+dis[lugar], out=np.zeros_like(pops), where=dis[lugar]!=0)
            aux = atratividade * localFer
            if np.sum(aux) == 0:
                break
            prob = aux / np.sum(aux)
            aux2 = rd.random()
            aux3 = 0
            for i in range(len(prob)):
                aux3+=prob[i]
                if aux2 < aux3:
                    self.totalPops+=pops[i]
                    self.dist+=dis[lugar][i]
                    self.popsDist=self.totalPops / self.dist
                    self.caminho.append(cidIndex[i])
                    self.percentPops = self.totalPops/totalPops
                    self.citiesVisited+=1
                    self.popsDistPercent = self.popsDist*(1+(self.percentPops+(self.citiesVisited/27)))
                    for k in self.caminho[1:]:
                        self.sumOfFer = localFer[index[k]]
                    self.sumOfFer/=len(self.caminho)
                    break
            if self.citiesVisited>10 or self.percentPops>0.6:
                break



def getValue(e):
    return e[0]

## Main
NUMITER, NUMANTS, CITY, FERO,EVAP, colonia = initializer()
bestCaminho = []

for i in range(NUMITER):
    if i %100 == 0:
        print(i)
    for ant in colonia:
        ant.calcularCaminho()
        if bestCaminho == []:
            bestCaminho.append([ant.popsDistPercent, ant.popsDist, ant.caminho.copy(), ant.sumOfFer])
        else:
            teste = False
            for resultados in bestCaminho:
                if [ant.popsDist, ant.caminho] == [resultados[0], resultados[2]]:
                    teste=True
                    break
            if teste == True:
                bestCaminho.append([ant.popsDistPercent, ant.popsDist, ant.caminho.copy(), ant.sumOfFer])
        ant.caminho = [CITY]
    bestCaminho.sort(reverse = True, key=getValue)
    bestCaminho = bestCaminho[0:3]
    pares = []

    for resultados in bestCaminho:
        aux2 = []
        for individuos in range(len(resultados[2])):
            if individuos == len(resultados[2])-1:
                pares.append([aux2.copy(), resultados[3]])
                break
            else:
                aux = [resultados[2][individuos], index[resultados[2][individuos+1]]]
                aux2.append(aux.copy())

    for cidade in capitais_estaduais:
        for aresta in range(len(feromonio[cidade])):
            escolhido = False
            for par in pares:
                if [cidade, aresta] in par[0]:
                    feromonio[cidade][aresta] = (1-EVAP) * feromonio[cidade][aresta] + par[1]
                    escolhido=True
                    break
            if escolhido == False:
                feromonio[cidade][aresta]*=(1-EVAP)


for i in bestCaminho:
    print(i)
'''
for i in feromonio:
    print(feromonio[i])
'''





