class Queue:
	"""A simple queue to show classes"""

	def __init__(self, item=[]):
		self.queue = []
		if type(item) is list:
			#Ignore PART of this line, unless you want me to go into the Python object model...
			self.queue = list(item)
		else:
			self.queue.append(item)

	def enqueue(self, item):
		self.queue.append(item)
		return len(self.queue)

	def dequeue(self):
		if self.length() == 0:
			return
		value = self.queue[0]
		self.queue = self.queue[1:]
		return value

	def length(self):
		return len(self.queue)

#Don't pay attention to this right now
if __name__ == "__main__":
	
	#But please pay attention to this part
	print "Making first queue"
	x = Queue()
	print x.enqueue('a')
	print x.enqueue('b')

	print x.length()

	# print x.dequeue()
	# print x.dequeue()

	print "Making second queue"
	y = Queue('c')

	print y.length()
	print y.enqueue('d')

	print y.length()

	print y.dequeue()
	print y.dequeue()

	print x.dequeue()
	print x.dequeue()

	print "Making thrid queue"
	z = Queue(['e', 'f', 'g'])

	print z.length()

	print z.dequeue()
	print z.dequeue()
	print z.dequeue()