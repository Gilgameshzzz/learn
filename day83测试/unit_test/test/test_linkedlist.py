# Filename  : test_linkedlist.py
# Date  : 2018/11/14
import unittest

from un.LLinkedList import LinkedList


class TestLinkedList(unittest.TestCase):
	def test_append(self):
		l = LinkedList()
		# self.assertTrue(l.size() == 0)
		l.append(1)
		self.assertTrue(l.size() == 1)

		l.append(2)
		self.assertTrue(l.size() == 2)
		for i in range(3, 99):
			l.append(i)

		self.assertTrue(l.size() == 98)

		# item = l.find(0)
		# self.assertEqual(item, 1)

		l.insert(100, 50)
		self.assertTrue(l.size() == 99)

		self.assertTrue(l.index(100) == 50)

		l.delete(50)
		self.assertTrue(l.size() == 98)


if __name__ == '__main__':
	unittest.main()