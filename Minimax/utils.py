def printMatrix(matrix):
    for i in range(0, 3):
        for j in range(0, 3):
            print(matrix[i][j], end='\t')
        print('\n')
    print('\n')

def evaluate(matrix):
    
    # Checking for Rows for X or O victory.  
    for row in range(0, 3):  
        if matrix[row][0] == matrix[row][1] and matrix[row][1] == matrix[row][2]:  
            if matrix[row][0] == 'x': return 10 
            elif matrix[row][0] == 'o': return -10 
  
    # Checking for Columns for X or O victory.  
    for col in range(0, 3):  
        if matrix[0][col] == matrix[1][col] and matrix[1][col] == matrix[2][col]:  
            if matrix[0][col]=='x': return 10 
            elif matrix[0][col] == 'o': return -10 
  
    # Checking for Diagonals for X or O victory.  
    if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:  
        if matrix[0][0] == 'x': return 10 
        elif matrix[0][0] == 'o': return -10 

    if matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:  
        if matrix[0][2] == 'x': return 10 
        elif matrix[0][2] == 'o': return -10 
       
    # Else if none of them have won then return 0  
    return 0 
   
def isFullOf(matrix):
    for i in range(0, 3):
        for j in range(0, 3):
            if(matrix[i][j] == '_') :
                return False
    return True

def minimax(matrix, person = 'x'):
    score = evaluate(matrix)
    if(score or (score == 0 and isFullOf(matrix))): 
        return score
    
    if(person == 'x'):
        bestValue = -1000

        for i in range(0, 3):
            for j in range(0, 3):
                if(matrix[i][j] == '_'):
                    matrix[i][j] = 'x'
                    best = minimax(matrix, 'o')
                    bestValue = max(bestValue, best)
                    matrix[i][j] = '_'

        # i = int(input("Enter X: "));
        # j = int(input("Enter Y: "));

        # if(matrix[i][j] == '_'):
        #     matrix[i][j] = 'x'
        #     best = minimax(matrix, 'o')
        #     bestValue = max(bestValue, best)
        #     matrix[i][j] = '_'

        return bestValue
    else :
        bestValue = 1000
        for i in range(0, 3):
            for j in range(0, 3):
                if(matrix[i][j] == '_'):
                    matrix[i][j] = 'o'
                    best = minimax(matrix, 'x')
                    bestValue = min(bestValue, best)
                    matrix[i][j] = '_'
        return bestValue

def findBestMove(matrix, person = 'x'):
    bestValue = 1000
    position = (0, 0, 0)
    for i in range(0, 3):
        for j in range(0, 3):
            if(matrix[i][j] == '_'):
                matrix[i][j] = 'o'
                best = minimax(matrix, 'x')
                matrix[i][j] = '_'
                if(best < bestValue) :
                    position = (i, j, best)
                    bestValue = best
    return position