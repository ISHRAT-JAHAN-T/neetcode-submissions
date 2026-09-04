class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        #row_search 

      #  print(len(board)) 
       
        col = 0
        for j in range(len(board[col])): 
            seen = set() 
            for i in range(len(board)):
            
                #print("column number", board[i][j])
                col = col+1  
                if board[i][j] != ".":
                    if board[i][j] not in seen: 
                        seen.add(board[i][j])
                    else: 
                        return False    
            #print("\n")   

        #search by colum 
        for i in range(len(board)): 
            seen = set() 
            for j in range(len(board[i])): 
                #print(board[i][j])  
                if board[i][j] != '.':
                    if board[i][j] not in seen: 
                        seen.add(board[i][j])
                    else: 
                        return False
        #3*3 row by column 
       # print("hellow world")
        for i in range(0,len(board),3): 
            seen = set()
            #print("row")
            for j in range (0,len(board[i]),3): 
               #print("col")
                seen = set()
                
                for k in range(i,i+3): 
                    for l in range(j,j+3): 
                        #print(board[k][l], end = " ")
                        if board[k][l] != '.': 
                           if board[k][l] not in seen: 
                                seen.add(board[k][l])
                           else: 
                                return False    
                           
                    



          
            



        return True
        