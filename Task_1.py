class Student:
  ID = 0

  def __init__(self,name,dept, age,cgpa):
    self.name = name
    self.age = age
    self.cgpa = cgpa
    self.dept = dept
    Student.ID += 1

  def showDetails(self):
    print(f'ID : {Student.ID} \nName: {self.name} \nDepartmemnt : {self.dept}')
    print(f"Age: {self.age} \nCGPA: {self.cgpa}")

  @classmethod
  def from_String(cls,string):
    name, dept, age, cgpa = string.split("-")
    return Student(name,dept,age,cgpa)

s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails() 
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails() 
