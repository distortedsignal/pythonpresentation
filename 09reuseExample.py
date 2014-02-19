#from 07classExample import Queue as Q

Q = __import__('07classExample').Queue

class QueueManager:
	
	def __init__(self, queues=[]):
		if "" in queues:
			return False

		self.queueDictionary = {}
		for queueName in queues:
			self.queueDictionary[queueName] = Q()

	def enqueue(self, queue="", item=""):
		if queue == "":
			return False
		self.queueDictionary[queue].enqueue(item)
		return self.queueDictionary[queue].length()

	def dequeue(self, queue=""):
		if queue == "":
			return False
		return self.queueDictionary[queue].dequeue()

	def countQueues(self):
		return len(self.queueDictionary)

	def queueLength(self, queueName=""):
		if queueName == "":
			return False
		return self.queueDictionary[queueName].length()

	def newQueue(self, queueName=""):
		if queueName == "":
			return False
		self.queueDictionary[queueName] = Q()

def blankFunction(self):
	print "This is a function"


#Again, don't pay attention to this
if __name__ == "__main__":
	#Ok, start paying more attention
	qm1 = QueueManager()
	qm1.newQueue("queueA")
	qm1.enqueue("queueA", "Message 1")
	qm1.newQueue("queueB")
	qm1.enqueue("queueB", "Message a")
	qm1.enqueue("queueA", "Message 2")
	qm1.enqueue("queueB", "Message b")
	
	print "Total number of queues", qm1.countQueues()
	print "First message in Queue A: ", qm1.dequeue("queueA")
	print "Second message in Queue A: ", qm1.dequeue("queueA")
	print "\nCurrent length of Queue B: ", qm1.queueLength("queueB")
	print "First message in Queue B: ", qm1.dequeue("queueB")
	print "Current length of Queue B", qm1.queueLength("queueB")
	print "Second message in Queue B: ", qm1.dequeue("queueB")
	print "Current length of Queue B", qm1.queueLength("queueB")

	qm1.newQueue(blankFunction)
	qm1.enqueue(blankFunction, "Message Alpha")
	qm1.enqueue(blankFunction, "Message Beta")
	print "\nFirst message in function queue", qm1.dequeue(blankFunction)
	print "\nSecond message in function queue", qm1.dequeue(blankFunction)
