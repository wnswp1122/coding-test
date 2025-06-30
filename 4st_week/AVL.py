class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)


    def ll_rotate(self, z):  # 오른쪽 회전
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))       

        return y

    def rr_rotate(self, z):  # 왼쪽 회전
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def lr_rotate(self, root):  # LR 회전
        root.left = self.rr_rotate(root.left)
        return self.ll_rotate(root)

    def rl_rotate(self, root):  # RL 회전
        root.right = self.ll_rotate(root.right)
        return self.rr_rotate(root)

    def balance_node(self, root):
        balance = self.get_balance(root)        

        # LL
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.ll_rotate(root)

        # LR
        if balance > 1 and self.get_balance(root.left) < 0:
            return self.lr_rotate(root)

        # RR
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rr_rotate(root)

        # RL
        if balance < -1 and self.get_balance(root.right) > 0:
            return self.rl_rotate(root)

        return root

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        return self.balance_node(root)

    def min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        # 1. 일반 이진 탐색 트리 삭제
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # key == root.key 인 경우: 삭제 대상 노드

            # 자식 1개 혹은 0개
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # 자식 2개인 경우: 오른쪽 서브트리에서 최소값 노드로 대체
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # 2. 삭제 후 높이 갱신
        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. 균형 맞춤
        return self.balance_node(root)

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.key] + self.inorder(root.right)


# 테스트
avl = AVLTree()
root = None

# 삽입
for k in [20, 10, 30, 5, 14, 25, 40]:
    root = avl.insert(root, k)

print("중위 순회 (삽입 후):", avl.inorder(root))

# 삭제
root = avl.delete(root, 10)
print("중위 순회 (10 삭제 후):", avl.inorder(root))

root = avl.delete(root, 30)
print("중위 순회 (30 삭제 후):", avl.inorder(root))

root = avl.delete(root, 20)
print("중위 순회 (20 삭제 후):", avl.inorder(root))
