class Student:
	def __init__(self ,name ,roll ,marks):
		self.name=name
		self.roll=roll
		self.marks=marks

	def average(self):
		return sum(self.marks) / len(self.marks)

	def grade(self):
		averages=self.average()
		if averages >=90:
			return "A"
		elif averages >=75:
			return "B"
		elif averages >=60:
			return "C"
		else :
			return "Fail"

	def display(self):
		print(f"Name:{self.name} and Roll:{self.roll}")
		print(f"Marks={self.marks}")
		print(f"Average={self.average():.2f} and Grade={self.grade()}")

s1 = Student("Ravi", 101, [85, 90, 78])
s2 = Student("Priya", 102, [92, 88, 95])
s3 = Student("Arjun", 103, [60, 55, 70])
s4 = Student("Sneha", 104, [45, 50, 40])
s5 = Student("Kiran", 105, [75, 80, 72])

students=[s1 , s2 ,s3 ,s4 ,s5 ]

for s in students:
	print(s.display())
	print("_"*25)