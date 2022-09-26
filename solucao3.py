from cmath import inf

mapa = [list(linha.rsplit()) for linha in open("casos de teste/teste50.txt")]

tamanho = int(mapa[0][0])

movY, movX = [-1, -1, 0], [0, 1, 1]
caminho = [["x" for x in range(tamanho)] for y in range(tamanho + 1)]

for y in range(1, tamanho + 1):
    for x in range(tamanho - 1, -1, -1):
        vizinhos = []
        if mapa[y][x] == "x":
            continue

        if y == 1 and x == tamanho - 1:
            caminho[y][x] = int(mapa[y][x])
        
        else:
            casinhaAtual = int(mapa[y][x])
            for i in range(3):
                
                newY = y + movY[i]
                newX = x + movX[i]
                try:
                    novaCasinha = caminho[newY][newX]
                    vizinho = casinhaAtual + int(novaCasinha)
                    vizinhos.append(vizinho)
                except:
                    vizinhos.append(-inf)
            caminho[y][x] = max(vizinhos)
            
for linha in caminho:
    print(linha)
    
print("Resultado:", caminho[tamanho][0])

