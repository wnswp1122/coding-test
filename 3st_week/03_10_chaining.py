class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v
            
class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):        
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)


    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

def test_linked_dict():
    d = LinkedDict()
    
    # 삽입
    d.put("apple", 1)
    d.put("banana", 2)
    d.put("cherry", 3)
    d.put("date", 4)
    d.put("apple", 5)  # 중복 키 테스트 (현재 구조에서는 중복 허용됨)

    # 조회 테스트
    assert d.get("apple") == 1, "apple에 대해 첫 값을 반환해야 함"
    assert d.get("banana") == 2, "banana 값 조회 실패"
    assert d.get("cherry") == 3, "cherry 값 조회 실패"
    assert d.get("date") == 4, "date 값 조회 실패"
    assert d.get("nonexistent") is None, "존재하지 않는 키에 대해 None을 반환해야 함"

    print("모든 테스트 통과!")  

test_linked_dict()

