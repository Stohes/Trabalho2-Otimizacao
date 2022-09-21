map = [list(line.rsplit()) for line in open("casos de teste/teste1.txt")]

size = int(map[0][0])
start = map[size][0]
end = map[1][size - 1]


movY, movX = [-1, -1, 0], [0, 1, 1]
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
            else: # botar o for antigo
                walk(y - 1, x, novoGold, caminho + " N")
                walk(y - 1, x + 1, novoGold, caminho + " NE")
                walk(y, x + 1, novoGold, caminho + " E")


walk(size, 0, 0, "")
print(maiorGold)
print(melhorCaminho)
