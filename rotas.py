import requests
import numpy as np
import random as rd
from getCitizens import capitais_estaduais, index

## inicialização das matrizes e variáveis utilizadas no algorítmo
pops = np.load("pops.npy")
fileDis = np.load("popPerDist.npy", allow_pickle=True)
dis = fileDis.item(0)
feromonio = {}
cidIndex = list(index.keys())
for i in capitais_estaduais:
    aux = np.zeros(27)
    aux[index[i]] = 1
    feromonio[i] = np.ones(27) - aux

for i in dis:
    dis[i][dis[i]>1600000] = 0

def initializer():
    NUMOFANTS = int(input("Number of ants to simulate: "))
    print(index)
    STARTCITY = cidIndex[int(input("Select starting city: "))]
    FERMONTOTAL = 27*27-27
    colonia = []
    for ants in range(NUMOFANTS):
        colonia.append(ANTS(STARTCITY))
    print(colonia)
    return [NUMOFANTS, STARTCITY, FERMONTOTAL]

class ANTS:
    def __init__(self, initialLoc):
        self.caminho = [initialLoc]
        self.pops = pops[index[initialLoc]]
        self.dist = 0
    def arrayDiv(self, list1 , list2):
        if len(a) != len(b):
            raise ("list1 and list2 must have same length")
        size = len(a)
        for i in range(size):
            ...

    def calcularCaminho(self):
        lugar = self.caminho[-1]
        atratividade = np.divide(pops, dis[lugar], out=np.zeros_like(pops), where=dis[lugar]!=0)
        aux = atratividade * feromonio[lugar]
        prob = aux / np.sum(aux)
        aux2 = rd.random()
        aux3 = 0
        for i in prob:
            aux3+=i
            if aux2 < aux3:
                return cidIndex[prob.index(i)]

a = ANTS("São Paulo")
print(a.caminho, a.dist, a.pops, a.calcularCaminho())
