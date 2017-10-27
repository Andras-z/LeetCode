'''Sort a linked list in O(n log n) time using constant space complexity.
'''
#Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	# merge sort, recursively 
	def sortList(self, head):
		if not head or not head.next:
			return head
		# divide list into two parts
		fast, slow = head.next, head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
		second = slow.next
		# cut down the first part
		slow.next = None
		l = self.sortList(head)
		r = self.sortList(second)
		return self.merge(l, r)

	# merge in-place without dummy node
	def merge(self, l, r):
		if not l or not r:
			return l or r
		if l.val > r.val:
			l, r = r, l
		# get the return node "head"
		head = pre = l
		l = l.next
		while l and r:
			if l.val < r.val:
				pre.next = l
				l = l.next
			else:
				pre.next = r
				r = r.next
			pre = pre.next
		# l and r at least one is None
		pre.next = l or r
		return head

class Solution2(object):
	def merge(self, h1, h2):
		dummy = tail = ListNode(None)
		while h1 and h2:
			if h1.val < h2.val:
				tail.next, tail, h1 = h1, h1, h1.next
			else:
				tail.next, tail, h2 = h2, h2, h2.next
	
		tail.next = h1 or h2
		return dummy.next
	
	def sortList(self, head):
		if not head or not head.next:
			return head
	
		pre, slow, fast = None, head, head
		while fast and fast.next:
			pre, slow, fast = slow, slow.next, fast.next.next
		pre.next = None

		return self.merge(*map(self.sortList, (head, slow)))