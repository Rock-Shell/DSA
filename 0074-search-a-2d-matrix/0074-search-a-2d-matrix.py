class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search(arr):
            s = 0
            e = len(arr)-1
            while s<=e:
                mid = (s+e)//2
                if arr[mid] > target:
                    e = mid-1
                elif arr[mid] == target:
                    return True
                else:
                    s = mid+1
                print(mid, s, e)
            return False

        for m in matrix:
            if bin_search(m):
                return True
        return False