class Solution:
    def subsets(self, nums: list[int]):  # -> List[List[int]]:
        queue = []
        result = []
        for i in range(len(nums)):
            queue.append([nums[i]])

        return queue


nums = [1, 2, 3]
sol = Solution()
print(sol.subsets(nums))
