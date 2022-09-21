map = [list(line.rsplit()) for line in open("casos de teste/teste2.txt")]

size = int(map[0][0])
start = map[size][0]
end = map[1][size - 1]


movY, movX = [-1, -1, 0], [0, 1, 1]
maiorGold = 0


def walk(y, x, goldAtual):  # passar o 4 parametro como string do caminho atual
    global maiorGold

    if not (y < 1 or x > size - 1):  # sair do mapa

        casinhaAtual = map[y][x]

        if casinhaAtual != "x":
            novoGold = goldAtual + int(casinhaAtual)

            if y == 1 and x == size - 1:  # final
                if novoGold > maiorGold:
                    maiorGold = novoGold
            else: # testar o for antigo
                walk(y - 1, x, novoGold)
                walk(y - 1, x + 1, novoGold)
                walk(y, x + 1, novoGold)


walk(size, 0, 0)
print(maiorGold)
