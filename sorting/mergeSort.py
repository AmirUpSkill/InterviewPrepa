from typing import List

class Solution:
    def mergeSort(self, nums: List[int]) -> List[int]:
        def merge(left: List[int], right: List[int]) -> List[int]:
            i, j = 0, 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1
            return result

        if len(nums) <= 1:
            return nums
            
        mid = len(nums) // 2
        left_half = self.mergeSort(nums[:mid])
        right_half = self.mergeSort(nums[mid:])
        return merge(left_half, right_half)

    def test_solution(self):
        # Test case 1: Regular unsorted list
        assert self.mergeSort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

        # Test case 2: Already sorted list
        assert self.mergeSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

        # Test case 3: List with duplicate elements
        assert self.mergeSort([5, 2, 8, 12, 1, 5]) == [1, 2, 5, 5, 8, 12]

        print("All test cases passed!")

# Run the tests
Solution().test_solution()
