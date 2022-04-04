# 리스트를 활용한 간단한 해쉬 테이블 구현

hash_table = list([0 for i in range(8)])  # 해쉬 테이블 공간 생성


def get_key(data):  # 해쉬 키 생성
    return hash(data)  # 내장함수


def hash_function(key):  # Division을 이용한 간단한 해쉬 함수
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))  # 해쉬 함수로 산출한 해쉬 주소
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


"""
위에 구현한 해쉬 함수는 데이터를 저장할 때 중복된 해쉬 주소가 생성될 경우(충돌), 데이터를 덮어써버리는 문제가 발생한다.

충돌 해결을 위한 방법
1. 연결리스트를 이용해 데이터를 추가로 뒤에 연결시켜 저장하는 기법 (Open hashing)
2. 충돌이 일어난 해쉬 주소의 다음 주소들 중 빈 공간에 데이터를 저장하는 기법 (Close Hashing)
"""
