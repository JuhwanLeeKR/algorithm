# Close Hashing 기법을 적용한 hash table (리니어 기법)
hash_table = list([0 for i in range(8)])  # 해쉬 테이블 공간 생성


def get_key(data):  # 해쉬 키 생성
    return hash(data)


def hash_function(key):  # Division을 이용한 간단한 해쉬 함수
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    # 1. 해쉬 충돌이 발생할 경우 (해쉬 주소가 동일한 경우)
    if hash_table[hash_address] != 0:
        # 충돌이 일어난 주소부터 끝까지 스캔한다
        for index in range(hash_address, len(hash_table)):
            # 동일한 key일 경우 덮어쓴다
            if hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
            # 빈 공간을 찾으면 저장한다
            elif hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
    # 2. 해쉬 충돌이 발생하지 않으면 그 공간에 데이터(key와 value)를 저장한다
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index][0] == index_key:
                return hash_table[index][1]
            # 빈 공간이 나올 때까지 동일한 key를 발견하지 못하면 데이터가 없는 것
            elif hash_table[index] == 0:
                return None
    else:
        return None


"""
* 시간 복잡도
해쉬 테이블의 시간 복잡도는 충돌이 없을 경우 O(1), 충돌이 모두 발생할 경우 O(n) 이다. 일반적으로 충돌이 없을 경우를 기대하고 만들기 때문에 시간 복잡도는 O(1) 이라고 말할 수 있다
"""
