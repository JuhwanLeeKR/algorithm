# https://leetcode.com/problems/binary-search/


class Solution:
    def search(self, nums: list[int], target: int):  # -> int:
        def binary_search_while(array, target, start, end):
            while start <= end:
                mid = (start + end) // 2

                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return None

        start = 0
        end = len(nums) - 1

        result = binary_search_while(nums, target, start, end)
        if result == None:
            return -1
        else:
            return result


nums = [-1, 0, 3, 5, 9, 12]
target = 9
sol = Solution()
print(sol.search(nums, target))
