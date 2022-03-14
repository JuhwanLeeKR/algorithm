# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# https://leetcode.com/problems/valid-parentheses/

'''
Example 1:

Input: s = "()"
Output: true
'''

# python을 이용할 때는 list로 stack을 만들면된다
# 하지만 다른 언어를 사용할 때는 방식이 다르다


class Solution:
    def isValid(self, s: str) -> bool:
