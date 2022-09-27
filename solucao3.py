from cmath import inf

mapa = [list(linha.rsplit()) for linha in open("casos de teste/teste1.txt")]

tamanho = int(mapa[0][0])

movY, movX = [-1, -1, 0], [0, 1, 1]
resultados = [[-100000000 for x in range(tamanho)] for y in range(tamanho + 1)]

for y in range(1, tamanho + 1):
    for x in range(tamanho - 1, -1, -1):
        vizinhos = []
        if mapa[y][x] == "x":
            continue

        if y == 1 and x == tamanho - 1:
            resultados[y][x] = int(mapa[y][x])
        
        else:
            casinhaAtual = int(mapa[y][x])
            for i in range(3):
                
                newY = y + movY[i]
                newX = x + movX[i]
                try:
                    novaCasinha = resultados[newY][newX]
                    vizinho = casinhaAtual + int(novaCasinha)
                    vizinhos.append(vizinho)
                except:
                    vizinhos.append(-inf)
            resultados[y][x] = max(vizinhos)
      
caminho = ""
y = tamanho
x = 0
while True:
    
    if y == 1 and x == tamanho - 1:
        break
        
    try:
        cima = int(resultados[y - 1][x])
    except:
        cima = -100000000
        
    try:
        diagonal = int(resultados[y - 1][x + 1])
    except:
        diagonal = -100000000
        
    try:
        direita = int(resultados[y][x + 1])
    except:
        direita = -100000000
        
    maiorVizinho = max(cima, diagonal, direita)
    
    if maiorVizinho == cima:
        y -= 1
        caminho += "N "
    if maiorVizinho == diagonal:
        y -= 1
        x += 1
        caminho += "NE "
    if maiorVizinho == direita:
        x += 1
        caminho += "E "
        
            
            
            
            
for linha in resultados:
    print(linha)
    
print("Ouro:", resultados[tamanho][0])

print("Caminho:", caminho)

