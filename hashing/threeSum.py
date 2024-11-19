from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        hash_map={}
        my_set=set()
        for i , num in enumerate(nums):
            hash_map[num]=i
        for i in range(n):
            for j in range(i+1,n):
                current_sum=-nums[i]-nums[j]
                if current_sum in hash_map and hash_map[current_sum]!=i and hash_map[current_sum]!=j:
                    my_set.add(tuple(sorted([nums[i],nums[j],current_sum])))
        return my_set

    def test_threeSum(self):
        # Test case 1: Standard case with multiple solutions
        assert self.threeSum([-1,0,1,2,-1,-4]) == {(-1,-1,2), (-1,0,1)}
        
        # Test case 2: No solution
        assert self.threeSum([0,1,1]) == set()
        
        # Test case 3: All zeros
        assert self.threeSum([0,0,0]) == {(0,0,0)}
        
        print("All test cases passed!")

# Run the tests
if __name__ == "__main__":
    Solution().test_threeSum()
