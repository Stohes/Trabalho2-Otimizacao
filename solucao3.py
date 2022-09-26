from cmath import inf


map = [list(line.rsplit()) for line in open("casos de teste/teste10.txt")]

size = int(map[0][0])
start = map[size][0]
end = map[1][size - 1]

movY, movX = [-1, -1, 0], [0, 1, 1]
caminho = [["x" for x in range(size)] for y in range(size + 1)]


for y in range(1, size + 1):
    for x in range(size - 1, -1, -1):
        maxGold = []
        if map[y][x] == "x":
            continue

        if y == 1 and x == size - 1:
            caminho[y][x] = int(map[y][x])
        
        else:
            casinhaAtual = int(map[y][x])
            for i in range(3):
                
                newY = y + movY[i]
                newX = x + movX[i]
                try:
                    novaCasinha = caminho[newY][newX]
                    vizinho = casinhaAtual + int(novaCasinha)
                    maxGold.append(vizinho)
                except:
                    maxGold.append(-inf)
            caminho[y][x] = max(maxGold)
            
            
            
            
            
            # for i in range(3):
            #     newY = y + movY[i]
            #     newX = x + movX[i]
            #     if newY > size or newX < 0:
            #         maxGold.append(-10000000)
            #     else:
            #         novaCasinha = map[newY][newX]
            #         if novaCasinha == "x":
            #             continue
            #         vizinho = casinhaAtual + int(novaCasinha)
            #         maxGold.append(vizinho)
            # caminho[y][x] = max(maxGold)
            
            
            
            
            
            
            
            
            # if y > 1:
            #     cima = casinhaAtual + int(caminho[y - 1][x])
            # else:
            #     cima = -1000000

            # if y > 1 and x < size - 1:
            #     diagonal = casinhaAtual + int(caminho[y - 1][x + 1])
            # else:
            #     diagonal = -1000000

            # if x < size - 1:
            #     direita = casinhaAtual + int(caminho[y][x + 1])
            # else:
            #     direita = -1000000

            # caminho[y][x] = max(cima, diagonal, direita)
            
for line in caminho:
    print(line)
    
print(caminho[size][0])


# startTime = time.time()
# endTime = time.time()
# print(endTime - startTime)
