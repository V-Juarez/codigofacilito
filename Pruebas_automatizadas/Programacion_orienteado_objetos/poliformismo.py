def retornaElMayor(a,b):
# isinstance()
    if isinstance(a,int) and isinstance(b,int):
        if a > b:
            return a
        return b
    if isinstance(a,str) and isinstance(b,str):
        #return [a,b].sort()[0]
        palabras = [a,b]
        palabras.sort()
        return palabras[0]
    if isinstance(a,list) and isinstance(b,list):
        if len(a) > len(b):
            return a
        return b

#print(retornaElMayor(10,200))
#print(retornaElMayor("Victor","Alenjandro"))
print(retornaElMayor( [1,2,3], [1,2,3,4,5] ))
