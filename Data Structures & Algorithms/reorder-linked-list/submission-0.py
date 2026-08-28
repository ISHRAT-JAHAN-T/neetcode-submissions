class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        array_list = []

        while head:
            array_list.append(head)
            head = head.next

        left = 0
        right = len(array_list) - 1

        while left < right:
            array_list[left].next = array_list[right]
            left += 1

            if left == right:
                break

            array_list[right].next = array_list[left]
            right -= 1

        array_list[left].next = None