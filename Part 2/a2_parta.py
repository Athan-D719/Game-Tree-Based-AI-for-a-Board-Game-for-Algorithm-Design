#    Main Author(s): Jonathan Diaz, Jurgen Bueno
#    Main Reviewer(s): Seyed Iman Modarres Sadeghi



class HashTable:

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice as long as it is a hash table			

	#Node for linked list in Hash Table.
	class Node:
		def __init__(self, key, value):
			self.key = key
			self.value = value
			self.next = None
        
		def get_value(self):
			return self.value
		
		def get_key(self):
			return self.key
		
		def set_value(self, value):
			self.value = value
	
	def __init__(self, cap=32):
		self.cap = cap
		self.size = 0
		self.table = [None] * cap

	#given a key value pair it generates the hash an looks for it in a node as to insert it in that corresponding linked list
	#Pre-condition: if size goes above the given load factor(0.7), resizing operation is needed.
	def insert(self, key, value):
		
		if (self.size / self.cap) > 0.7: #load factor
			self.resize()

		hash_value = hash(key) % self.cap  #hashes key with corresponsing length(int) within the bounds of the capacity.
		node = self.table[hash_value]

		if node is None:
			self.table[hash_value] = self.Node(key, value)
			self.size += 1
			return True
		
		#collision -> traversion
		while node.next is not None: 
			if node.get_key() == key:
				return False
			node = node.next

		if node.get_key() == key:
			return False
		else:
			node.next = self.Node(key, value)
			self.size += 1
		
		return True

	#Looks into table with the hashed_value through the given key, modifies corresonding node in linked list. 
	def modify(self, key, value):
		hash_value = hash(key) % self.cap
		node = self.table[hash_value]

		while node is not None:
			if node.get_key() == key:
				node.set_value(value) #modifies existing record
				return True 
			node = node.next

		return False

	#Looks into table with the hashed_value through the given key, if key node found, previous node takes the next as the following node.
	def remove(self, key):
		hash_value = hash(key) % self.cap
		node = self.table[hash_value]
		prev = None

		while node is not None:
			if node.get_key() == key:
				if prev is None: #first node
					self.table[hash_value] = node.next
				else: #node found in table with values
					prev.next = node.next
				self.size -= 1
				return True
			prev = node
			node = node.next
		return False

	#Looks for node with key in table thorugh hashed value. when row found, uses node.next iteration.
	def search(self, key):
		hash_value = hash(key) % self.cap
		node = self.table[hash_value]

		while node is not None:
			if node.get_key() == key:
				return node.get_value()
			node = node.next
		return None
	
	#capacity looked into value. could need resizing. Uses Resizing if size is over load factor.
	def capacity(self):
		if (self.size / self.cap) > 0.7: #last piece of the puzzle (look for resize)
			self.resize()
		return self.cap
	
	def __len__(self):
		return self.size

	#doubles capacity -> triggered by load factor over 0.7.
	def resize(self):
		temp_cap = self.cap * 2
		temp_table = [None] * temp_cap

		for i in range(self.cap):
			node = self.table[i]
			while node is not None: #for each node (till the last)

				hash_value = hash(node.get_key()) % temp_cap #gets key and hashes

				if temp_table[hash_value] is None: #(key-value pair insertion)
					temp_table[hash_value] = self.Node(node.get_key(), node.get_value())
				else:
					current = temp_table[hash_value]  #(key-value pair aggregation)
					while current.next is not None: #till last.
						current = current.next
					current.next = self.Node(node.get_key(), node.get_value())

				node = node.next

		#resized values returned along with table.
		self.cap = temp_cap
		self.table = temp_table