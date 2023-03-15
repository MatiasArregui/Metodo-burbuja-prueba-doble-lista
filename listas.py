# from random import *
# lista1=sorted(sample(range(0,99),10))
# print(lista1)
# lista3=sample(range(0,200),10)
# print(lista3)
# lista2=[x for x in lista3 if x%2 == 0]
# print(lista2)
# lista2.sort()
# print(lista2)

def unificaOrdena(lista1,lista2):
    listaNuvea=[]
    a=len(lista1)
    b=len(lista2)
    cont=0
    while a>cont<b:
        if lista1[cont] < lista2[cont]:
            listaNuvea.append(lista1[cont])
        if lista1[cont] > lista2[cont]:
            listaNuvea.append(lista2[cont])
        cont+=1
    if a>cont:
        listaNuvea.extend(lista1)
    if b>cont:
        listaNuvea.extend(lista2)
    return listaNuvea

def ordena(lista1,lista2):
    listaNueva=[]
    listaNueva.extend(lista1)
    listaNueva.extend(lista2)
    a=len(lista1)
    b=len(lista2)
    if a>b:
        for x in range(a-1):
            for y in range(a-1):
                if listaNueva[y] > listaNueva[y+1]:
                    listaNueva[y], listaNueva[y+1]= listaNueva[y+1], listaNueva[y]
    if a<b:
        for x in range(b-1):
            for y in range(b-1):
                if listaNueva[y] > listaNueva[y+1]:
                    listaNueva[y], listaNueva[y+1]= listaNueva[y+1], listaNueva[y]
    c=len(listaNueva)
    for x in range(c-1):
        for y in range(c-1):
            if listaNueva[y] > listaNueva[y+1]:
                listaNueva[y], listaNueva[y+1]= listaNueva[y+1], listaNueva[y]
    return listaNueva

matias=[20,21,22,23,24]
david=[16,17,18,19]
print(unificaOrdena(matias,david))
nahuel=[2,1,3,4,5]
abril=[2,1,4,5,6,7]
print(ordena(nahuel,abril))
