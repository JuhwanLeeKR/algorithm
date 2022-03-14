# Node와 Stack이 필요하다
class Node:
    # Node는 두 가지로 구성이 된다. 내가 가지고 있는 값(item)과 가리키고 있는 값(next)
    def __init__(self, item, next):
        # 나의 item은 item 이다
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        # Stack을 처음 만들었을 때는 top이 None 이다.
        self.top = None

    # push, pop, is_emtpy 3개가 존재해야한다.

    # 비었는지 안 비었는지 어떻게 알까?
    def is_emtpy(self):
        # 이 녀석의 top이 none인지 아닌지 보면 된다. bool 값
        return self.top is None

    # 밀어 넣을 때는 어떻게 할까?
    def push(self, val):
        # 기존의 top이  지정 대상이다(self.top)
        self.top = Node(val, self.top)

    # 값을 꺼낼때
    def pop(self):
        # 비어있는지 안 비었는지에 따라 다르다
        # 오류를 방지 위해 if not이 필요하다
        if not self.top:
            return None
        # 비어있지 않다면 top을 node로 꺼내준다
        node = self.top
        # 새로운 top을 기존 아래에 있는 것으로 지정을 해준다
        self.top = self.top.next

        return node.item
