from cmath import inf
import time
map = [list(line.rsplit()) for line in open("casos de teste/teste2.txt")]

size = int(map[0][0])
start = map[size][0]
end = map[1][size - 1]

movY, movX = [-1, -1, 0], [0, 1, 1]
caminho = [[0 for x in range(size)] for y in range(size + 1)]

for y in range(1, size + 1):
    for x in range(size - 1, -1, -1):
        
        if map[y][x] == "x":
            continue

        if y == 1 and x == size - 1:
            caminho[y][x] = int(map[y][x])
        
        else:
            casinhaAtual = int(map[y][x])
            if y > 1:
                cima = casinhaAtual + int(caminho[y - 1][x])
            else:
                cima = 0

            if y > 1 and x < size - 1:
                diagonal = casinhaAtual + int(caminho[y - 1][x + 1])
            else:
                diagonal = 0

            if x < size - 1:
                direita = casinhaAtual + int(caminho[y][x + 1])
            else:
                direita = 0

            caminho[y][x] = max(cima, diagonal, direita)
    
print(caminho[size][0])


# startTime = time.time()
# endTime = time.time()
# print(endTime - startTime)
