# 1. 1 ~ 10000 배열을 만들자
# 2. 1부터 10000
from tokenize import Number


numSet = set(range(1, 10000))
remove = set()

for i in range(1, 10001):
    # 셀프넘버 함수 생성
    for num in str(i):  # string이면 for문을 돌 수 있다.
        i += int(num)

    if i < 10000:
        remove.add(i)  # set에 int를 넣으려면 add로 넣는다.

self_number = numSet - remove
for num in sorted(self_number):
    print(num)
