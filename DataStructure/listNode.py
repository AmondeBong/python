class ListNode:
    def __init__(self, newItem, nextNode: 'ListNode'):  # nextNode가 ListNode임을 방어적으로 알려줌
        self.item = newItem
        self.next = nextNode
