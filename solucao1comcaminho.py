map = [list(line.rsplit()) for line in open("casos de teste/teste1.txt")]

size = int(map[0][0])
start = map[size][0]
end = map[1][size - 1]


movY, movX, direction = [-1, -1, 0], [0, 1, 1], [" N", " NE", " E"]
maiorGold = 0
melhorCaminho = ""


def walk(y, x, goldAtual, caminho):
    global maiorGold
    global melhorCaminho

    if not (y < 1 or x > size - 1):  # sair do mapa

        casinhaAtual = map[y][x]

        if casinhaAtual != "x":
            novoGold = goldAtual + int(casinhaAtual)

            if y == 1 and x == size - 1:  # final
                if novoGold > maiorGold:
                    maiorGold = novoGold
                    melhorCaminho = caminho
            else:
                for i in range(3):
                    newY = y + movY[i]
                    newX = x + movX[i]
                    walk(newY, newX, novoGold, caminho + direction[i])


# def walk2(y, x):
#     maxGold = []
#     path = ""
#     if y < 1 or x > size - 1:
#         return 0

#     casinhaAtual = map[y][x]
#     if casinhaAtual == "x":
#         return 0

#     if y == 1 and x == size - 1:
#         return int(casinhaAtual)

#     for i in range(3):
#         newY = y + movY[i]
#         newX = x + movX[i]
#         gold = int(casinhaAtual) + walk2(newY, newX)[0]
#         maxGold.append(gold)
#         path += direction[i]
#     return max(maxGold), path

walk(size, 0, 0, "")
print(maiorGold)
print(melhorCaminho)

# print(walk2(size, 0))