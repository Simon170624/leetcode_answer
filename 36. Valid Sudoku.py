#### test
board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
'''
for r in range(0, 9):
    nums = set()
    for c in range(0, 9):
        if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
            print(1, False)
        if board[r][c] != '.' and board[r][c] not in nums:
            nums.add(board[r][c])
        elif board[r][c] != '.' and board[r][c] in nums:
            print(2, False)

for c in range(0, 9):
    nums = set()
    for r in range(0, 9):
        if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
            print(3, False)
        if board[r][c] not in nums:
            nums.add(board[r][c])
        else:
            print(4, False)

for r in range(0, 3):
    nums = set()
    for c in range(0, 3):
        if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
            print(5, False)
        if board[r][c] not in nums:
            nums.add(board[r][c])
        else:
            print(6, False)
'''  
nums = set()      
for r in range(0, 3):
    for c in range(3, 6):
        if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
            print(1, False)
        if board[r][c] != '.' and board[r][c] not in nums:
            nums.add(board[r][c])
        elif board[r][c] != '.' and board[r][c] in nums:
            print(2, False)
'''     
for r in range(0, 3):
    nums = set()    
    for c in range(6, 9):
        if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
            print(9, False)
        if board[r][c] not in nums:
            nums.add(board[r][c])
        else:
            print(10, False)

for r in range(3, 6):
    nums = set() 
    for c in range(0, 3):
        if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
            print(11, False)
        if board[r][c] not in nums:
            nums.add(board[r][c])
        else:
            print(12, False)
        
for r in range(3, 6):
    nums = set()
    for c in range(3, 6):
        if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
            print(13, False)
        if board[r][c] not in nums:
            nums.add(board[r][c])
        else:
            print(14, False)
        
for r in range(3, 6):
    nums = set()    
    for c in range(6, 9):
        if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
            print(15, False)
        if board[r][c] not in nums:
            nums.add(board[r][c])
        else:
            print(16, False)

for r in range(6, 9):
    nums = set()
    for c in range(0, 3):
        if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
            print(17, False)
        if board[r][c] not in nums:
            nums.add(board[r][c])
        else:
            print(18, False)
        
for r in range(6, 9):
    nums = set()
    for c in range(3, 6):
        if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
            print(19, False)
        if board[r][c] not in nums:
            nums.add(board[r][c])
        else:
            print(20, False)
    
for r in range(6, 9):
    nums = set()
    for c in range(6, 9):
        if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
            print(21, False)
        if board[r][c] not in nums:
            nums.add(board[r][c])
        else:
            print(22, False)
'''
print(True)

#### most brust force
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(0, 9):
            nums = set()
            for c in range(0, 9):
                if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
                    return False
                if board[r][c] != '.' and board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != '.' and board[r][c] in nums:
                    return False
        
        for c in range(0, 9):
            nums = set()
            for r in range(0, 9):
                if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
                    return False
                if board[r][c] != '.' and board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != '.' and board[r][c] in nums:
                    return False
                
        nums = set()
        for r in range(0, 3):
            for c in range(0, 3):
                if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
                    return False
                if board[r][c] != '.' and board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != '.' and board[r][c] in nums:
                    return False
                
        nums = set()
        for r in range(0, 3):
            for c in range(3, 6):
                if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
                    return False
                if board[r][c] != '.' and board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != '.' and board[r][c] in nums:
                    return False
                
        nums = set()        
        for r in range(0, 3):    
            for c in range(6, 9):
                if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
                    return False
                if board[r][c] != '.' and board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != '.' and board[r][c] in nums:
                    return False
                
        nums = set()
        for r in range(3, 6):
            for c in range(0, 3):
                if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
                    return False
                if board[r][c] != '.' and board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != '.' and board[r][c] in nums:
                    return False
                
        nums = set()        
        for r in range(3, 6):
            for c in range(3, 6):
                if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
                    return False
                if board[r][c] != '.' and board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != '.' and board[r][c] in nums:
                    return False
                
        nums = set()        
        for r in range(3, 6):
            for c in range(6, 9):
                if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
                    return False
                if board[r][c] != '.' and board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != '.' and board[r][c] in nums:
                    return False
                
        nums = set()
        for r in range(6, 9):
            for c in range(0, 3):
                if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
                    return False
                if board[r][c] != '.' and board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != '.' and board[r][c] in nums:
                    return False
                
        nums = set()        
        for r in range(6, 9):
            for c in range(3, 6):
                if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
                    return False
                if board[r][c] != '.' and board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != '.' and board[r][c] in nums:
                    return False
                
        nums = set()    
        for r in range(6, 9):
            for c in range(6, 9):
                if board[r][c] != '.' and (int(board[r][c]) <= 0 or int(board[r][c]) > 9):
                    return False
                if board[r][c] != '.' and board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != '.' and board[r][c] in nums:
                    return False
        
        return True

#### smarter solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set([]) for i in range(9)]
        col = [set([]) for i in range(9)]
        grid = [set([]) for i in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False

                g = r // 3 * 3 + c // 3
                if board[r][c] in grid[g]:
                    return False
                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])

        return True