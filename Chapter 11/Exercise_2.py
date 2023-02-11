#11-3 Employee:
class Employee:
    def __init__(self,first,last,salary=0):
        self.first = first
        self.last = last
        self.salary = salary 

    def give_raise(self,increase=5000):
        self.salary = self.salary + increase

