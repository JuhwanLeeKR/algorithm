# 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# 1. 특정 알파벳수가 짝수(even)면 max-length(return값)에 전부 추가
# 2. 특정 알파벳수가 3이상의 홀수(odd)면 max-length(return값)에 전부 추가 -1

s = "abccccdd"


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Tip) string에 set을 사용하면 중복을 제거해주고 집합으로 바뀐다.
        # Tip) string에 list를 사용하면 하나씩 나눠 주고 list로 바뀐다.
        # s를 set을 이용하여 중복을 제거해 주고 list로 만들어준다.
        arr = list(set(s))  # ['d', 'c', 'b', 'a']
        # s를 list로 만들어준다.
        arrString = list(s)  # ['a', 'b', 'c', 'c', 'c', 'c', 'd', 'd']
        # count 변수 선언 (result 값)
        count = 0
        for el in arr:
            # # Tip) list에 count 함수를 사용하면 특정 요소 개수를 구할 수 있다.
            # 만약에 arrString의 특정 개수가 짝수라면
            if arrString.count(el) % 2 == 0:
                # count에 그 수만큼 추가
                count += arrString.count(el)
            # 만약에 arrString의 특정 개수가 홀수라면
            elif arrString.count(el) % 2 == 1:
                # count에 그 수 -1 만큼 추가
                count += arrString.count(el) - 1
        # 홀수가 있는 경우 1을 다시 더해줘야합니다.
        for el in arr:
            if arrString.count(el) % 2 == 1:
                count += 1
                # 한 번만 실행되게 for문을 종료 시킵니다.
                break
        print(count)
        return count


solve = Solution()
print(solve.longestPalindrome(s))
