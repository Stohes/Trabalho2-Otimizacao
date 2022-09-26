from cmath import inf
mapa = [list(linha.rsplit()) for linha in open("casos de teste/teste10.txt")]

size = int(mapa[0][0])
inicio = mapa[size][0]
fim = mapa[1][size - 1]

movY, movX = [-1, -1, 0], [0, 1, 1]

casinhasVisitadas = {}
def walk(y, x):
    vizinhos = []
    if inicio == "x" or fim == "x":
        return "Mapa inválido"
    
    if y < 1 or x > size - 1:
        return -inf

    coordenadasAtuais = f"{y} {x}"
    if coordenadasAtuais in casinhasVisitadas:
        return casinhasVisitadas.get(coordenadasAtuais)
    
    else:
        casinhaAtual = mapa[y][x]
        if casinhaAtual == "x":
            return -inf

        if y == 1 and x == size - 1:
            return int(casinhaAtual)

        for i in range(3):
            newY = y + movY[i]
            newX = x + movX[i]
            ouro = int(casinhaAtual) + walk(newY, newX)
            vizinhos.append(ouro)
            casinhasVisitadas.update({coordenadasAtuais: max(vizinhos)})
        return max(vizinhos)
    

print("Resultado:", walk(size, 0))
