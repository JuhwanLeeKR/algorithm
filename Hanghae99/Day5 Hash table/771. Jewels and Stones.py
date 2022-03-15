# https://leetcode.com/problems/jewels-and-stones/
'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1.
Input: jewels = "aA", stones = "aAAbbbb" Output: 3
Example 2.
Input: jewels = "z", stones = "ZZ" Output: 0

-> 요약: 해시(해시 테이블/맵, 딕셔너리)를 사용하여 주어진 문제를 풀 수 있는지

1. jewels: 각 글자는 보석에 해당하는 돌을 나타냅니다.
2. stones: 각 글자는 내가 보유하고 있는 돌을 나타냅니다.
3. 내가 갖고 있는 돌 중 보석이 몇 개나 있는지를 반환합니다.
4. 'a'와 'A'는 서로 다른 종류의 돌로 간주합니다.
- jewels 및 stones의 길이는 50이하 정수입니다.
- 영문만 고려하면 됩니다.
'''

# jewels = "aA"
# stones = "aAAbbbb"
jewels = "zaaeZ"
stones = "ZZzk"


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str):
        # jewels과 stones가 string 형식으로 들어오게 됩니다.
        # 1. jewels 의 값을 뽑아내자
        # 2. stones를 key-value(dictioinary)로 변환 시키자.
        jewelList = list(jewels)
        stoneList = list(stones)
        # alphabet을 key로 받고 갯수를 value로 받자.
        # 개수를 담아줄 변수를 선언합니다.
        stoneCount = {}
        # try, except로 갯수를 찾습니다.
        # 웹개발 종합반 python 서버 작업
        for i in stoneList:
            try:
                stoneCount[i] += 1
            except:
                stoneCount[i] = 1

        jewelCount = 0
        for i in range(len(jewelList)):
            # 보석명을 확인해줍니다.
            jewel = jewelList[i]  # 1: a, 2: b
            # 보석이 없는 경우를 고려해줍니다.
            try:
                jewelCount += stoneCount[jewel]
            except:
                pass

        return jewelCount


sol = Solution()
print(sol.numJewelsInStones(jewels, stones))
