class Solution:

    def heapify(self, a, i, n):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and a[left] > a[largest]:
            largest = left

        if right < n and a[right] > a[largest]:
            largest = right

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.heapify(a, largest, n)

    def heapsort(self, a):
        n = len(a)

        for i in range(n//2 - 1, -1, -1):
            self.heapify(a, i, n)

        for i in range(n - 1, 0, -1):
            a[0], a[i] = a[i], a[0]

            self.heapify(a, 0, i)

        return a
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapsort(nums)
