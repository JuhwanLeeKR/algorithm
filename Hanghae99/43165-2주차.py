"""
n개의 음이 아닌 정수들
순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만든다.
numbers = 사용할 수 있는 숫자가 담긴 배열(2-20개) (1-50)
target = 타겟 넘버(1-1000)

"""


def solution(numbers, target):
    answer = 0
    range(len(numbers))  # 0 ~ len(numbers)까지의 길이
    """
    경우의 수 = 2^len(numbers)
    
    numbers[0] + numbers[1] + ... + numbers[len(numbers)]
    ...
    -numbers[0] - numbers[1] - ... - numbers[len(numbers)]
    
    target과 일치하면 answer += 1
    """
    return answer
