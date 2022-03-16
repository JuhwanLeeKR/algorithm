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
- jewels는 문자열 중복이 없기에 set을 사용하지 않아도 됩니다.
'''

# jewels = "aA"
# stones = "aAAbbbb"


jewels = "zaEeZ"
stones = "ZZzk"


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str):
        # jewels과 stones가 string 형식으로 들어오게 됩니다.
        # 1. jewels 의 값을 뽑아내자
        # 2. stones를 key-value(dictioinary)로 변환 시키자.
        #    -> {알파벳: 수, 알파벳: 수, ...}
        # 3. stones에 있는 jewel의 개수를 파악하자.
        jewelList = list(jewels)  # ['z', 'a', 'E', 'e', 'Z']
        stoneList = list(stones)  # ['Z', 'Z', 'z', 'k']

        # 해시 테이블을 선언해 줍니다.
        stoneCount = {}
        # 웹개발 종합반 python 서버 작업 활용
        # try, except로 개수를 찾습니다.
        for i in stoneList:
            try:
                stoneCount[i] += 1
            except:
                stoneCount[i] = 1
                # stoneCount = {'Z': 2, 'z': 1, 'k': 1}

        # 보석 개수를 저장하기 위한 변수를 선언해줍니다.
        jewelCount = 0

        # jewelList의 길이 만큼 반복을 해줍니다.
        for i in range(len(jewelList)):
            # jewel이란 변수에 보석 명을 저장해줍니다.
            # 변수로 따로 저장해주지 않으면 error가 뜨게됩니다.
            jewel = jewelList[i]  # 1: z, 2: a, 3: E, 4:e, 5:Z
            # try except를 사용하여 keyerror를 방지해줍니다.
            try:
                jewelCount += stoneCount[jewel]  # ex) stoneCount['z'] = 1
            # 보석이 없는 경우를 고려해줍니다.
            except:
                # pass는 에러가 발생해도 무시하고 넘어가 줍니다.
                pass

        return jewelCount


'''
jewels = "zaEeZ"
stones = "ZZzk" => 3이 print 될 것입니다.(z: 1개 ,Z: 2개)
'''

sol = Solution()
print(sol.numJewelsInStones(jewels, stones))
