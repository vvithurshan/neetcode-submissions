class Solution:
    def BinarySearch(self, matrix, row, target):
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            mid = (l + r + 1)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (l + r + 1)//2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return self.BinarySearch(matrix, mid, target)
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False