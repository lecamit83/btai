from utils import minimax,findBestMove,printMatrix, isFullOf
def person(matrix):
    while True:
        x = int(input('X: '))
        y = int(input('Y: '))
        if(matrix[x][y] == '_'): break
        print('Position has value... Try again...')
        
    matrix[x][y] = 'x'    
    printMatrix(matrix)


def computer(matrix, x, y):
    matrix[x][y] = 'o'    
    printMatrix(matrix)


if __name__ == '__main__':

    board = [
        ['_', '_', '_'],  
        ['_', '_', '_'],  
        ['_', '_', '_']
    ]  
    # value = minimax(board, 'o')
    # print(value)
    printMatrix(board)
    while True:
        person(board)
        position = findBestMove(board)
        computer(board, position[0], position[1])        
        if(position[2] == 10):
            print('CLIENT WIN')
            break 
        
        if(position[2] == -10):
            print('COMPUTER WIN')
            break
        
        if(position[0] == 0 and isFullOf(board)):
            print('DRAW')
            break
        
    # print(position[0])


