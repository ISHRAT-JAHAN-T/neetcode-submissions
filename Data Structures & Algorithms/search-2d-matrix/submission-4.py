class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  
        top = 0 
        bottom = len(matrix)-1
        while(top<bottom):  
            
            mid = (top + bottom) // 2
            print("top bottom mid", top, bottom, mid)

            print("mid",matrix[mid]) 
            #check target has in the mid row 
            left_midRow = 0 
            right_midRow = len(matrix[mid])- 1 
            last_digit= right_midRow

            print("left_midRow", left_midRow)
            print("right_midRow", right_midRow) 

            while(left_midRow < right_midRow): 
                mid_midRow = (left_midRow+right_midRow) // 2 
                print(" left_midRow, right_midROw,mid_midRow",left_midRow,right_midRow,  mid_midRow)
                if matrix[mid][mid_midRow] == target: 
                    return True 
                elif matrix[mid][mid_midRow] < target: 
                    left_midRow = mid_midRow + 1 
                else: 
                    right_midRow = right_midRow - 1  
            print("did not find in mid row")
            print(right_midRow,left_midRow)
            if left_midRow == right_midRow: 
                print("last part")
                if matrix[mid][left_midRow] == target: 
                    return True

            if matrix[mid][last_digit] < target : 
                top = mid+1 
            else: 
                bottom = mid - 1  

        print("hellow world")        
        if top == bottom:  
            print("top&bottom",matrix[top])
            left_midRow = 0 
            right_midRow = len(matrix[top])- 1 
            last_digit= right_midRow

            print("left_midRow", left_midRow)
            print("right_midRow", right_midRow) 

            while(left_midRow < right_midRow): 
                mid_midRow = (left_midRow+right_midRow) // 2 
                if matrix[top][mid_midRow] == target: 
                    return True 
                elif matrix[top][mid_midRow] < target: 
                    left_midRow = mid_midRow + 1 
                else: 
                    right_midRow = right_midRow - 1  
            if left_midRow == right_midRow: 
                print("last part")
                if matrix[top][left_midRow] == target: 
                    return True
               


        return False      



    

            

    