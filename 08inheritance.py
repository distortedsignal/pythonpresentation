class RootClass:
	rootVarOne = 1
	rootVarTwo = []

	def methodOne(self, item=0):
		self.rootVarTwo.append(item)

class ChildClassOne(RootClass):
	childVarOne = 2

	def methodTwo(self, item=5):
		self.rootVarOne += item
		self.childVarOne += item

class ChildClassTwo(RootClass):
	childVarTwo = 3

	def methodTwo(self, item=7):
		self.rootVarOne += item
		self.childVarTwo += item

class GrandchildClass(ChildClassOne, ChildClassTwo):
	grandchildVar = 0

	def methodThree(self, item=10):
		self.rootVarOne += item
		self.grandchildVar += item


print "\n\nRoot Class:"
root = RootClass()

print "Root var 1: ", root.rootVarOne, "\nRoot var 2: ", root.rootVarTwo

root.methodOne(10)

print "\nRoot var 2: ", root.rootVarTwo

print "\n\nChild Class 1"

child1 = ChildClassOne()

print "Root var 1: ", child1.rootVarOne, "\nRoot var 2: ", child1.rootVarTwo, "\nChild var 1: ", child1.childVarOne

child1.methodOne()
child1.methodTwo()

print "\nRoot var 1: ", child1.rootVarOne, "\nRoot var 2: ", child1.rootVarTwo, "\nChild var 1: ", child1.childVarOne

print "\n\nChild Class 2"

child2 = ChildClassTwo()

print "Root var 1: ", child2.rootVarOne, "\nRoot var 2: ", child2.rootVarTwo, "\nChild var 2: ", child2.childVarTwo

child2.methodOne()
child2.methodTwo()

print "\nRoot var 1: ", child2.rootVarOne, "\nRoot var 2: ", child2.rootVarTwo, "\nChild var 2: ", child2.childVarTwo

print "\n\nGrandchild Class"

gChildClass = GrandchildClass()

print "Root var 1: ", gChildClass.rootVarOne, "\nRoot var 2: ", gChildClass.rootVarTwo, "\nChild var 1: ", gChildClass.childVarOne, "\nChild var 2: ", gChildClass.childVarTwo, "\nGrandchild var: ", gChildClass.grandchildVar

gChildClass.methodOne()
gChildClass.methodTwo()
gChildClass.methodThree()

print "\nRoot var 1: ", gChildClass.rootVarOne, "\nRoot var 2: ", gChildClass.rootVarTwo, "\nChild var 1: ", gChildClass.childVarOne, "\nChild var 2: ", gChildClass.childVarTwo, "\nGrandchild var: ", gChildClass.grandchildVar
