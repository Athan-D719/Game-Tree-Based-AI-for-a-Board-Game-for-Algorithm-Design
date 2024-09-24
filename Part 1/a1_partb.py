#    Main Author(s): Seyed Iman Modarres Sadeghi
#    Main Reviewer(s):




class SortedList:

	class Node:
		def __init__(self, data, next = None, prev = None):
			self.data = data
			self.next = next
			self.prev = prev

		def get_data(self):
			return self.data

		def get_next(self):
			return self.next

		def get_previous(self):
			return self.prev

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def get_front(self):
		return self.head

	def get_back(self):
		return self.tail

	def is_empty(self):
		return self.length == 0

	def __len__(self):
		return self.length

	def insert(self,data):
		newNode = self.Node(data)
		self.length += 1

		if(self.head == None):
			self.head = newNode
			self.tail = newNode
			return newNode
		
		if(data < self.head.data):
			newNode.next = self.head
			self.head.prev = newNode
			self.head = newNode
			return newNode

		if(data > self.tail.data):
			newNode.prev = self.tail
			self.tail.next = newNode
			self.tail = newNode
			return newNode

		current = self.head
		while(True):
			if(current.data <= data and current.next.data >= data):
				current.next.prev = newNode
				newNode.next = current.next
				newNode.prev = current
				current.next = newNode
				return newNode
			
			current = current.next
		
	def erase(self,node):
		if(node == None):
			raise ValueError('Cannot erase node referred to by None')
		
		self.length -= 1
		
		if(node == self.head and node == self.tail):
			self.head = None
			self.tail = None
			return
		
		if(node == self.head):
			self.head.next.prev = None
			self.head = self.head.next
			return
		
		if(node == self.tail):
			self.tail.prev.next = None
			self.tail = self.tail.prev
			return
		
		node.prev.next = node.next
		node.next.prev = node.prev

	def search(self, data):
		if(self.head == None):
			return None

		current = self.head
		while(current != None and data > current.data):
			current = current.next

		if(current != None and data == current.data):
			return current

		return None

