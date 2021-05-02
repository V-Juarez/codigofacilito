lista = [1,2,3,4,5,6]
#for valor in range(1, 101, 2):
#    print(valor)

#for valor in range( len(lista) ):
    #print("indice:", indice, "valor:", lista[indice])

for indice, valor in enumerate(lista, 10):
    print("indice:", indice, "valor:", valor)
