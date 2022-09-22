map = [list(line.rsplit()) for line in open("casos de teste/teste2.txt")]

size = int(map[0][0])
start = map[size][0]
end = map[1][size - 1]


movY, movX = [-1, -1, 0], [0, 1, 1]


def walk(y, x, goldAtual):
    maiorGold = 0
    if not (y < 1 or x > size - 1):  # sair do mapa
        casinhaAtual = map[y][x]

        if casinhaAtual != "x":
            novoGold = goldAtual + int(casinhaAtual)

            if y == 1 and x == size - 1:  # final
                if novoGold > maiorGold:
                    maiorGold = novoGold
            else:
                for i in range(3):
                    newY = y + movY[i]
                    newX = x + movX[i]
                    walk(newY, newX, novoGold)
                    return maiorGold


def charValue(y, x, goldAtual):
    maiorGold = 0
    if not (y < 1 or x > size - 1):  # sair do mapa
        casinhaAtual = map[y][x]

        if casinhaAtual != "x":
            novoGold = goldAtual + int(casinhaAtual)

            if y == 1 and x == size - 1:  # final

                if novoGold > maiorGold:
                    maiorGold = novoGold
                else:
                    for i in range(3):
                        newY = y + movY[i]
                        newX = x + movX[i]
                        gold = walk(newY, newX, novoGold)
                        maiorGold += gold
                    return maiorGold

print(charValue(size, 0, 0))
