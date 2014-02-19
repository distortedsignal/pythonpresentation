from emp import Employee as E

class Division:

	def __init__(self):
		self.employees = list([])
		self.products = list([])

	def addEmployee(self, name, salary):
		self.employees.append(E(name, salary))

	def countEmployees(self):
		return len(self.employees)

if __name__ == "__main__":
	d = Division()
	d.addEmployee("Alby", 73286)
	print d.countEmployees()
	print d.employees[0].name, d.employees[0].salary
