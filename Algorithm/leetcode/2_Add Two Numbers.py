# 안되면참고링크 https://manakim.tistory.com/entry/PYTHON-listnode-%EC%83%9D%EC%84%B1-%EC%B6%94%EA%B0%80-leetnode-Add-Two-Numbers
# https://velog.io/@kgh732/Python-%EC%9C%BC%EB%A1%9C-%ED%91%B8%EB%8A%94-Leetcode2.Add-Two-Numbers
# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_value = 0
        l2_value = 0

        num = 1
        for i in l1:
            l1_value += i * num
            num *= 10
            
        print(f"l1_value = {l1_value}")

        num = 1
        for i in l2:
            l2_value += i * num
            num *= 10
        
        print(f"l2_value = {l2_value}")

        value = l1_value + l2_value
        l3 = []
        for i in reversed(str(value)):
            l3.append(i)
        return l3

        