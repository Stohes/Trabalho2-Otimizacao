from types import NoneType


map = [list(line.rsplit()) for line in open("casos de teste/teste2.txt")]

size = int(map[0][0])
start = map[size][0]
end = map[1][size - 1]


movY, movX = [-1, -1, 0], [0, 1, 1]


def walk(y, x):
    gold = 0
    maiorGold = 0

    if not (y < 1 or x > size - 1):  # sair do mapa
        casinhaAtual = map[y][x]

        if casinhaAtual != "x":
            
            for i in range(3):
                newY = y + movY[i]
                newX = x + movX[i]

                novoGold = walk(newY, newX)
                if novoGold is not None:
                    gold += novoGold

                    if gold > maiorGold:
                        maiorGold = gold

            return gold + int(casinhaAtual)

print(walk(size, 0))
