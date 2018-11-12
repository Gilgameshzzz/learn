class Stack:

	def __init__(self, max_size):
		self.max_size = max_size
		self.alist = []

	def push(self, item):
		if self.size < self.max_size:
			self.alist.append(item)
		else:
			print('栈溢出')

	def pop(self):
		if not self.alist:
			self.alist.pop(0)
			print('删除成功')
		else:
			print('栈是空的')

	def index(self, item):
		if item in self.alist:
			list_copy = self.alist.copy()
			list_copy.reverse()
			for i in range(len(self.alist)):
				if item == list_copy[i]:
					print('该元素的索引为%s' % i)
					break
		else:
			print('该元素没有在栈中')

	def empty(self):
		self.alist = []

	def full(self):
		max_size = len(self.alist)
		self.max_size = max_size

	def size(self):
		print('当前栈大小为%s' % len(self.alist))

	def get(self, index):
		list_copy = self.alist.copy()
		list_copy.reverse()
		list_copy = list_copy[index:]
		print(list_copy[0])


class Node:

	def __init__(self, value):
		self.value = value
		self.next_node = None

	def set_next_node(self, node):
		self.next_node = node


# 链表
class LinkedList:

	def __init__(self, value):
		self.value = value
		self.head = None

	def append(self, value):
		pass

	def insert(self, value, index):
		pass

	def delete(self, index):
		pass

	def size(self):
		pass

	def remove(self, value):
		pass

	def index(self, value):
		pass

	def __repr__(self):
		pass


node1 = Node('carmack')
node2 = Node('jon')
node3 = Node('lisa')

head = node1
node1.set_next_node(node2)
node2.set_next_node(node3)

# while(head.next_node):
#     print(head.value)
#     head = head.next_node

while (True):
	print(head.value)
	if not head.next_node:
		break
	head = head.next_node

l = LinkedList()
l.append(4)
l.append(8)
l.append(9)
print(l)
