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


"""
책을 참고해보니
파이썬에서는 이진 검색을 지원하는 bisect 모듈을 제공한다.

https://docs.python.org/ko/3/library/bisect.html
"""
import bisect


def search(self, nums: list[int], target: int):
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1
