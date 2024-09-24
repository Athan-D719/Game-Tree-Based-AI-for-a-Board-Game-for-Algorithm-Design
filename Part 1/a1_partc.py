#    Main Author(s): Jonathan Diaz, Seyed Iman Modarres Sadeghi
#    Main Reviewer(s): 



class Stack:
	def __init__(self, cap=10):
		self.cap = cap
		self.list = [None] * cap #set up length
		self.size = 0

	def capacity(self):
		return self.cap
	
	def push(self, data): #add
		if len(self) == self.capacity():
			self.list += [None] * self.cap
			self.cap *= 2

		self.list[len(self)] = data
		self.size += 1

	def pop(self):
		if self.size == 0:
			raise IndexError('pop() used on empty stack')
		
		removedValue = self.list[self.size - 1]
		self.list[self.size - 1] = None
		self.size -= 1

		return removedValue

	def get_top(self):
		return self.list[self.size - 1]

	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size


class Queue:
	def __init__(self, cap = 10):
		self.cap = cap
		self.list = [None] * cap #same as before
		self.size = 0
		self.head = 0
		self.tail = 0

	def capacity(self):
		return self.cap

	def enqueue(self, data): #add
		newTail = (self.tail + 1) % self.cap
		if(self.list[newTail] != None):
			newList = self.list[self.head:]
			newList += self.list[:self.head]

			newList += [None] * self.cap
			self.list = newList
			newTail = self.cap
			self.cap *= 2

			self.head = 0

		if(self.size == 0):
			self.list[0] = data
			self.head = 0
			self.tail = 0
		else: 
			self.list[newTail] = data
			self.tail = newTail

		self.size += 1


	def dequeue(self):
		if self.size == 0:
			raise IndexError('dequeue() used on empty queue')
		
		past_head = self.list[self.head]
		self.list[self.head] = None
		self.head += 1

		self.size -= 1

		return past_head

	def get_front(self):
		return self.list[self.head]

	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size


class Deque:
	def __init__(self, cap = 10):
		self.cap = cap
		self.list = [None] * self.cap
		self.head = 0
		self.tail = 0
		self.size = 0

	def capacity(self):
		return self.cap

	def push_front(self, data):
		if(self.size == self.cap):
			newList = [None] * (self.cap * 2)
			newList[0] = data

			j = self.head
			for i in range(1, self.size + 1):
				newList[i] = self.list[j]

				if(j == self.size - 1):
					j = 0
				else:
					j += 1 
			self.list = newList			

			self.head = 0
			self.tail = self.size 

			self.cap *= 2


		elif(self.size == 0):
			self.list[0] = data

		else:
			if(self.head == 0):
				self.head = self.cap - 1
			else:
				self.head -= 1

			self.list[self.head] = data

		self.size += 1

	def push_back(self, data):
		if(self.size == self.cap):
			newList = [None] * (self.cap * 2)

			j = self.head
			for i in range(self.size):
				newList[i] = self.list[j]

				if(j == self.size - 1):
					j = 0
				else:
					j += 1 
			newList[self.size] = data
			self.list = newList			

			self.head = 0
			self.tail = self.size 

			self.cap *= 2


		elif(self.size == 0):
			self.list[0] = data

		else:
			if(self.tail == self.cap - 1):
				self.tail = 0
			else:
				self.tail += 1

			self.list[self.tail] = data

		self.size += 1

	def pop_front(self):
		if(self.size == 0):
			raise IndexError('pop_front() used on empty deque')
		
		removedValue = self.list[self.head]
		self.list[self.head] = None
		self.head = (self.head + 1) % self.cap

		self.size -= 1

		return removedValue

	def pop_back(self):
		if(self.size == 0):
			raise IndexError('pop_back() used on empty deque')
		
		removedValue = self.list[self.tail]
		self.list[self.tail] = None
		if(self.tail == 0):
			self.tail = self.cap - 1
		else:
			self.tail -= 1

		self.size -= 1

		return removedValue

	def get_front(self):
		return self.list[self.head]

	def get_back(self):
		return self.list[self.tail]

	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size

	def __getitem__(self, k):
		if(k >= self.cap):
			raise IndexError('Index out of range')
		
		return self.list[(self.head + k) % self.cap]
	