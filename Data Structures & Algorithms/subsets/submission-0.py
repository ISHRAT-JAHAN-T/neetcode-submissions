class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        subset = []

        def backtrack(i):

            # BASE CASE
            if i == len(nums):
                result.append(subset.copy())
                return

            # CHOICE 1: take nums[i]
            subset.append(nums[i])

            # EXPLORE
            backtrack(i + 1)

            # UNDO
            subset.pop()

            # CHOICE 2: don't take nums[i]
            backtrack(i + 1)

        backtrack(0)

        return result
        