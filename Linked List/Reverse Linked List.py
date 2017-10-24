'''Reverse a singly linked list.
'''
#Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList(self, head):
		prev = None
		while head:
			curr = head
			head = head.next
			curr.next = prev
			prev = curr
		return prev

	def reverseList2(self, head, prev = None):
		if not head:
			return prev
		n = head.next
		head.next = prev
		return self.reverseList2(n,head)