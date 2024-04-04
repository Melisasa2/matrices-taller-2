def rotar_matriz(matriz):
    return list(zip(*matriz))

def obtener_forma(matriz):
    if type(matriz) != list or not matriz:
        return []
    return [len(matriz), *obtener_forma(matriz[0])]

def multiplicar_matrices(matriz1, matriz2):
    matriz_rotada = rotar_matriz(matriz2)
    forma_matriz1 = obtener_forma(matriz1)
    forma_matriz2 = obtener_forma(matriz2)
    if forma_matriz1[1] != forma_matriz2[0]:
        return None
    producto = []
    altura_matriz1 = len(matriz1)
    for fila_matriz1 in range(altura_matriz1):
        fila_producto = []
        ancho_matriz_rotada = len(matriz_rotada)
        for columna_rotada in range(ancho_matriz_rotada):
            suma = 0
            for indice_elemento in range(len(matriz1[fila_matriz1])):
                suma += matriz1[fila_matriz1][indice_elemento] * matriz_rotada[columna_rotada][indice_elemento]
            fila_producto.append(suma)
        producto.append(fila_producto)
    return producto
