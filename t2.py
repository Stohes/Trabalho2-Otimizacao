map = [list(line.rsplit()) for line in open("casos de teste/teste2.txt")]
    
size = int(map[0][0])
start = map[size][0]
end = map[1][size -1]


movY, movX = [-1, -1, 0], [0, 1, 1]
gold = 0
maiorGold = 0

pathGold = []
def walk(y, x):
    maiorGold = 0
    casinhaAtual = map[y][x]
    
    if y == 1 and x == size - 1:  # end
        # if gold > maiorGold:
        #     maiorGold = gold
        pathGold.append(maiorGold)
    
    for i in range(3):
        newY = y + movY[i]
        newX = x + movX[i]
        
        if newY < 1 or newX > size - 1:
            continue
        
        novaCasinha = map[newY][newX]
        if novaCasinha != "x":
            gold = walk(newY, newX)
            maiorGold += gold
            
    return maiorGold
    

    


print(walk(3, 0))
print(pathGold)
