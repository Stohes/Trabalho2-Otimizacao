from cmath import inf
import sys

mapa = [list(linha.rsplit()) for linha in open("casos de teste/teste1.txt")]

tamanho = int(mapa[0][0])
inicio = mapa[tamanho][0]
fim = mapa[1][tamanho - 1]

if inicio == "x" or fim == "x":
    sys.exit("Mapa inválido")

movY, movX = [-1, -1, 0], [0, 1, 1]
resultados = [[-100000000 for x in range(tamanho)] for y in range(tamanho + 1)]

for y in range(1, tamanho + 1):
    for x in range(tamanho - 1, -1, -1):
        vizinhos = []
        if mapa[y][x] == "x":
            continue

        if y == 1 and x == tamanho - 1:
            resultados[y][x] = int(mapa[y][x])

        else:
            casinhaAtual = int(mapa[y][x])
            for i in range(3):

                newY = y + movY[i]
                newX = x + movX[i]
                try:
                    novaCasinha = resultados[newY][newX]
                    vizinho = casinhaAtual + int(novaCasinha)
                    vizinhos.append(vizinho)
                except:
                    vizinhos.append(-inf)
            resultados[y][x] = max(vizinhos)

caminho = ""
y = tamanho
x = 0
while True:

    if y == 1 and x == tamanho - 1:
        break

    cima, diagonal, direita = -100000000, -100000000, -100000000

    try:
        cima = int(resultados[y - 1][x])
        diagonal = int(resultados[y - 1][x + 1])
        direita = int(resultados[y][x + 1])
    except:
        pass

    maiorVizinho = max(cima, diagonal, direita)

    if maiorVizinho == cima:
        y -= 1
        caminho += "N "
    if maiorVizinho == diagonal:
        y -= 1
        x += 1
        caminho += "NE "
    if maiorVizinho == direita:
        x += 1
        caminho += "E "


for linha in resultados:
    print(linha)

print("Ouro:", resultados[tamanho][0])

print("Caminho:", caminho)
