from types import NoneType


map = [list(line.rsplit()) for line in open("casos de teste/teste2.txt")]

size = int(map[0][0])
start = map[size][0]
end = map[1][size - 1]


movY, movX = [-1, -1, 0], [0, 1, 1]


def walk(y, x, goldAtual, mG):
    maiorGold = mG
    
    if not (y < 1 or x > size - 1):  # sair do mapa
        casinhaAtual = map[y][x]

        if casinhaAtual != "x":
            novoGold = goldAtual + int(casinhaAtual)
            for i in range(3):
                newY = y + movY[i]
                newX = x + movX[i]
                maiorGold = walk(newY, newX, novoGold, maiorGold)
                
                if novoGold > maiorGold:
                    maiorGold = novoGold

    return maiorGold

print(walk(size, 0, 0, 0))
