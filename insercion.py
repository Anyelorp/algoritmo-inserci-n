def algoritmo_insercion(lista):
    
    for i in range(1, len(lista)):
        
        valor_actual = lista[i]
        
        j = i - 1
        while j >= 0 and valor_actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = valor_actual


mi_lista = [12, 11, 13, 5, 6]
algoritmo_insercion(mi_lista)
print("Lista ordenada:", mi_lista)
