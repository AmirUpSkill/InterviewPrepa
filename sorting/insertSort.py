class Solution:
    def solution(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
        return nums

    def test_solution(self):
        # Test case 1: Regular unsorted list
        assert self.solution([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

        # Test case 2: Already sorted list
        assert self.solution([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

        # Test case 3: List with duplicate elements
        assert self.solution([5, 2, 8, 12, 1, 5]) == [1, 2, 5, 5, 8, 12]

        print("All test cases passed!")

# Run the tests
Solution().test_solution()
