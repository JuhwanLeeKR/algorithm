# Open Hashing 기법을 적용한 hash table (체이닝 기법)
hash_table = list([0 for i in range(8)])  # 해쉬 테이블 공간 생성


def get_key(data):  # 해쉬 키 생성
    return hash(data)


def hash_function(key):  # Division을 이용한 간단한 해쉬 함수
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    # 1. 해쉬 충돌이 발생할 경우 ( 해쉬 주소가 동일할 경우 )
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            # 1-1. key가 동일하면 데이터를 덮어 쓴다
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        # 1-2. key가 동일하지 않으면 데이터를 연결해 저장한다.
        hash_table[hash_address].append([index_key, value])
    # 2. 해쉬 충돌이 발생하지 않으면 그 공간에(key, value)를 저장
    else:
        hash_table[hash_address] = [[index_key, value]]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None
