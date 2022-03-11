# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
# An Anagram is a word or phrase formed
# by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagrams(strs):
    # 빈 dictionary를 생성합니다.
    result = {}
    # strs의 모든 요소를 출력하여 확인합니다
    for i in strs:
        # sorted함수를 사용하여 list를 정렬합니다.
        #   -> sorted(정렬할 데이터, key 파라미터, reverse 파라미터)
        # join함수를 사용하여 list를 string으로 변환하고 x에 넣어줍니다.
        x = "".join(sorted(i))
        # print(x)
        if x in result:
            # result에 x값이 있으면 i를 value로 추가해줍니다.
            result[x].append(i)
        else:
            # result에 x가 없으면 key 값에 i를 추가해줍니다.
            result[x] = [i]
    # print(result.values())

    # result의 value 값을 가져와서 list로 만들어줍니다.
    arrAna = list(result.values())
    # sorted 함수를 이용해 arrAna를 오름차순으로 정렬합니다.
    arrAnaAscending = sorted(arrAna, key=len, reverse=False)
    print(arrAnaAscending)


groupAnagrams(strs)
