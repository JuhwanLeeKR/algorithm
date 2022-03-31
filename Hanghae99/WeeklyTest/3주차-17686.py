"""
정렬 lambda 사용

단순한 문자 코드 순이 아닌 파일명에 포함된 숫자를 반영한 정렬 기능 구현

파일명은 100글자 이내
영문 대소문자, 숫자, 공백, 마침표, 빼기

HEAD 숫자가 아닌 문자
NUMBER 한글자에서 최대 다섯 글자의 연속된 숫자 00000, 0101 가능
TAIL 숫자가 나올 수도 있고 아무 글자도 없을 수 있음

1. HEAD 사전식, 대소문자 구분X
2. 대소문자 차이 외에는 같을 경우 NUMBER 순 ( 9 < 10 < 0011 < 012 < 13 < 014 )
    0은 무시 012와 12는 같음
3. 둘다 같으면 원래 입력 순서 유지
"""


def solution(files):
    answer = []


# 다시 풀어볼 것.
# 1. isdigit(), isalpha(), isalnum() 함수 사용
# 2. 정규표현식 이용


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
"""
입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
"""
