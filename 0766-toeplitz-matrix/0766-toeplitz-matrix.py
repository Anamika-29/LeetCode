class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Validate Input
        if not matrix or not matrix[0]:
            return False                
        
        # Create a deque tracking the expected values for the next row
        expected = deque(matrix[0])
        
        # Iterate through all the remaining rows, verifying they align with the
        #   expected row.
        for row_i in range(1, len(matrix)):
            row = matrix[row_i]
            expected.pop()
            expected.appendleft(row[0])
            
			# Only check from index 1 and down as we've just added index 0 to expected
            for col_i in range(1, len(row)):
                if row[col_i] != expected[col_i]:
                    return False
        
        # If we've reached here, all diagonals aligned
        return True
        