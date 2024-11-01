import requests
import numpy as np
from getCitizens import capitais_estaduais, index

## inicialização das matrizes e variáveis utilizadas no algorítmo
pops = np.load("pops.npy")
fileDis = np.load("popPerDist.npy", allow_pickle=True)
dis = fileDis.item(0)
feromonio = {}
for i in capitais_estaduais:
    aux = np.zeros(27)
    aux[index[i]] = 1
    feromonio[i] = np.ones(27) - aux

for i in dis:
    dis[i][dis[i]>1600000] = 0


NUMOFANTS = input("Number of ants to simulate: ")
print(index)
STARTCITY = input("Select starting city: ")
FERMONTOTAL = 27*27-27

class ANTS:
    def __init__(initialLoc, ):
        self.caminho = [initialLoc]
        self.pops = pops[index[initialLoc]]
        self.dist = 0
    def arrayDiv(list1 , list2):
        if len(a) != len(b):
            raise ("list1 and list2 must have same length")
        size = len(a)
        for i in range(size):
            ...

    def calcularCaminho():
        lugar = self.caminho[-1]
        atratividade = np.divide(pops, dis[lugar], out=np.zeros_like(pops), where=dis[lugar]!=0)
        aux = atrativdade * feromonio[lugar]
        prob = aux / np.sum(aux)
        

#for ants in NUMOFANTS:
