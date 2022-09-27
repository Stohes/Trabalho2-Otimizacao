from cmath import inf
import sys
mapa = [list(linha.rsplit()) for linha in open("casos de teste/teste10.txt")]

tamanho = int(mapa[0][0])
inicio = mapa[tamanho][0]
fim = mapa[1][tamanho - 1]

if inicio == "x" or fim == "x":
    sys.exit("Mapa inválido")
    
movY, movX = [-1, -1, 0], [0, 1, 1]
resultados = [[-100000000 for x in range(tamanho)] for y in range(tamanho + 1)]

casinhasVisitadas = {}
def walk(y, x):
    vizinhos = []

    if y < 1 or x > tamanho - 1:
        try:
            resultados[y][x] = int(mapa[y][x])
            return -100000000
        except:
            return -100000000
    
    coordenadasAtuais = f"{y} {x}"
    if coordenadasAtuais in casinhasVisitadas:
        return casinhasVisitadas.get(coordenadasAtuais)
    
    else:
        casinhaAtual = mapa[y][x]
        if casinhaAtual == "x":
            return -100000000

        if y == 1 and x == tamanho - 1:
            resultados[y][x] = casinhaAtual
            return int(casinhaAtual)

        for i in range(3):
            newY = y + movY[i]
            newX = x + movX[i]
            ouro = int(casinhaAtual) + walk(newY, newX)
            vizinhos.append(ouro)
            casinhasVisitadas.update({coordenadasAtuais: max(vizinhos)})
        resultados[y][x] = max(vizinhos)
        return max(vizinhos)
    

print("Ouro:", walk(tamanho, 0))

caminho = ""
y = tamanho
x = 0
while True:

    if y == 1 and x == tamanho - 1:
        break

    try:
        cima = int(resultados[y - 1][x])
    except:
        cima = -100000000

    try:
        diagonal = int(resultados[y - 1][x + 1])
    except:
        diagonal = -100000000

    try:
        direita = int(resultados[y][x + 1])
    except:
        direita = -100000000

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
        
print("Caminho:", caminho)
