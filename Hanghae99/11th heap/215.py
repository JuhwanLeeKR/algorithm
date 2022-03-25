# https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
1. 일단 최대 힙을 만든다.
2. 최대값을 추출하는 방법을 k번 반복한다.
"""
import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int):  # -> int:
        return heapq.nlargest(k, nums)[-1]


nums = [3, 2, 1, 5, 6, 4]
k = 2
sol = Solution()
print(sol.findKthLargest(nums, k))
