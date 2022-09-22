import time
map = [list(line.rsplit()) for line in open("casos de teste/teste50.txt")]

size = int(map[0][0])
start = map[size][0]
end = map[1][size - 1]

movY, movX = [-1, -1, 0], [0, 1, 1]

caminho = ""
casinhasVisitadas = {}
def walk(y, x):
    maxGold = []
    if y < 1 or x > size - 1:
        return 0

    coordenadasAtuais = f"{y}{x}"
    if coordenadasAtuais in casinhasVisitadas:
        return casinhasVisitadas.get(coordenadasAtuais)
    
    else:
        casinhaAtual = map[y][x]
        if casinhaAtual == "x":
            return 0

        if y == 1 and x == size - 1:
            return int(casinhaAtual)

        for i in range(3):
            newY = y + movY[i]
            newX = x + movX[i]
            gold = int(casinhaAtual) + walk(newY, newX)
            maxGold.append(gold)
            casinhasVisitadas.update({coordenadasAtuais: max(maxGold)})
        return max(maxGold)


start = time.time()
print(walk(size, 0))
end = time.time()
print(end - start)