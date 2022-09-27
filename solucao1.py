from cmath import inf
import sys
mapa = [list(linha.rsplit()) for linha in open("casos de teste/teste10.txt")]

tamanho = int(mapa[0][0])
inicio = mapa[tamanho][0]
fim = mapa[1][tamanho - 1]

if inicio == "x" or fim == "x":
    sys.exit("Mapa inválido")

movY, movX = [-1, -1, 0], [0, 1, 1]

def walk(y, x):
    vizinhos = []
    
    if inicio == "x" or fim == "x":
        return "mapaa inválido"
    
    if y < 1 or x > tamanho - 1:
        return -inf

    casinhaAtual = mapa[y][x]
    if casinhaAtual == "x":
        return -inf
    
    if y == 1 and x == tamanho - 1:
        return int(casinhaAtual)

    for i in range(3):
        newY = y + movY[i]
        newX = x + movX[i]
        ouro = int(casinhaAtual) + walk(newY, newX)
        vizinhos.append(ouro)
    return max(vizinhos)

print("Resultado:", walk(tamanho, 0))
