class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row
        for i in range(len(board)):
            seen=set()
            for j in range(len(board[i])):
                value = board[i][j] 
                if not board[i][j].isdigit():
                    continue

                elif board[i][j] in seen: 
                    #print("duplicate from row")
                    return False
                
                seen.add(board[i][j])    
            #print() 
        #column
        for j in range(len(board[0])): 
            seen=set()
            
            for i in range(len(board)):  
                if not board[i][j].isdigit(): 
                    continue
                elif board[i][j] in seen: 
                   # print("duplicate from column")
                    return False
                seen.add(board[i][j])     

        #row,colum 3*3 
        for row_start in [0,3,6]: 
            for col_start in [0,3,6]: 
                seen=set()
                for i in range(row_start, row_start+3): 
                    for j in range(col_start,col_start+3): 
                        if not board[i][j].isdigit(): 
                            continue 
                        elif board[i][j] in seen: 
                            print("duplicate from 3*3")
                            return False 
                        seen.add(board[i][j])        





        return True