from Person import Person

class Employee(Person): #ChildClass/ SubClass
    def __init__(self, name, age, salary, sex):
        super().__init__(name, age, sex)
        self.salary = salary
    
    def display(self):
        # Method overriding
        print(self.name, self.age, self.salary)