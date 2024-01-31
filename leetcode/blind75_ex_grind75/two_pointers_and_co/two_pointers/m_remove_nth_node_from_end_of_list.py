from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leader = head
        while n:
            leader = leader.next
            n -= 1
        if leader is None:
            return head.next
        follower = head
        while leader.next:
            leader, follower = leader.next, follower.next
        follower.next = follower.next.next
        return head


if __name__ == "__main__":
    inputs = [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2),
        (ListNode(1), 1),
        (
            ListNode(
                1,
                ListNode(
                    2,
                ),
            ),
            2,
        ),
        (ListNode(1, ListNode(2, ListNode(3))), 3),
    ]
    s = Solution()
    for head, n in inputs:
        print(s.removeNthFromEnd(head, n))
