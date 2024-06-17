#   OOPS

class Employee:
     def __init__(self,name,salary):
          self.name = name
          self.salary = salary
         
     def getSalary(self):
          return self.salary
     
abc = Employee("Abc", "10000")
print(abc.salary)
print(abc.name)
