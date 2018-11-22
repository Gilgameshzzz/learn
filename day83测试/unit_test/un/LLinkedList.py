class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class LinkedList(object):

    def __init__(self, f_node=None):
        if f_node is not None:
            f_node = Node(f_node)
        self.head = f_node

    def append(self, node):
        """
        在链表最后增加节点
        :param node: 要增加的节点
        :return: None
        """
        node = Node(node)
        head = self.head
        if head is None:
            self.head = node
        else:
            link_size = self.size()
            last_node = self.find(link_size - 1)
            last_node.next_node = node

    def size(self):
        """
        返回链表长度
        :return: 链表长度
        """
        if self.head is None:
            raise IndexError('LinkedList is empty')
        else:
            count = 1
            head = self.head
            next_node = head.next_node
            while next_node:
                count += 1
                next_node = next_node.next_node
            return count

    def insert(self, node, index):
        """
        根据所给的节点和索引位置插入节点
        :param node: 要插入节点
        :param index: 插入位置
        :return: None
        """
        node = Node(node)
        head = self.head
        if head is None:
            raise IndexError('LinkedList is empty')
        else:
            if index == 0:
                node.next_node = self.head
            elif index == self.size():
                self.append(node)
            else:
                loc = 0
                next_node = head.next_node
                while next_node:
                    loc += 1
                    if index == loc:
                        back_node = self.find(loc - 1)
                        back_node.next_node = node
                        node.next_node = next_node
                        break
                    next_node = next_node.next_node

    def index(self, node):
        """
        根据传入节点返回节点所在的第一个位置
        :param node: 传入节点
        :return: 节点所在的第一个位置
        """
        head = self.head
        n = Node(node)
        if head is None:
            raise IndexError('LinkedList is empty')
        else:
            next_n = head
            num = 0
            while next_n:
                if next_n.value == n.value:
                    break
                num += 1
                next_node = next_n
                next_n = next_n.next_node
                if next_n is None:
                    if next_node != n:
                        return None
            return num

    def find(self, index):
        """
        根据所给索引查找节点
        :param index: 传入的索引
        :return: 索引位置对应节点
        """
        head = self.head
        if head is None:
            raise IndexError('LinkedList is empty')
        if index > self.size():
            raise IndexError('index out of range')
        if index < 0:
            raise IndexError('index out of range')
        else:
            next_n = head
            for num in range(self.size()):
                if index == num:
                    return next_n
                next_n = next_n.next_node

    def delete(self, index):
        """
        根据给出索引值删除节点
        :param index: 节点索引
        :return: None
        """
        if self.head is None:
            raise ValueError('LinkedList is empty')
        elif self.size() > 1:
            if index == 0:
                self.head = self.find(1)
            elif index == self.size() - 1:
                t_node = self.find(index - 1)
                t_node.next_node = None
            elif index >= self.size() or index < 0:
                raise IndexError('index out of range')
            else:
                del_node = self.find(index)
                del_node_next_node = del_node.next_node
                del_node_f_node = self.find(index - 1)
                del_node_f_node.next_node = del_node_next_node
        elif self.size() == 1:
            self.head = None

    def remove(self, node):
        """
        根据给定节点删除第一个节点
        :param node: 节点元素
        :return: None
        """
        node_index = self.index(node)
        if self.head is None:
            raise ValueError('LinkedList is empty')
        else:
            if node_index is None:
                raise ValueError('value not exit')
            else:
                if node_index == self.size() - 1:
                    t_node = self.find(self.index(node) - 1)
                    t_node.next_node = None
                elif node_index == 0:
                    self.head = self.find(1)
                else:
                    f_node = self.find(node_index - 1)
                    n_node = node.next_node
                    f_node.next_node = n_node

    def __str__(self):
        node = self.head
        if node is None:
            return 'empty LinkedList class: {}'.format(LinkedList)
        else:
            link_string = '<'
            while node:
                link_string = link_string + '{}'.format(node)
                node = node.next_node
                if node is not None:
                    link_string += ','
            link_string += '>'
            return link_string
