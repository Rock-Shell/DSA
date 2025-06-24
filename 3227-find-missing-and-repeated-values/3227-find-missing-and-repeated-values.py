class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        s = set()
        result = [-1, -1]
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in s:
                    s.add(grid[i][j])
                else:
                    result[0] = grid[i][j]

        for i in range(1,n*n+1):
            if i not in s:
                result[1] = i
        return result
