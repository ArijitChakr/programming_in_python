from Person import Person

class Student1(Person): #ChildClass/ SubClass
    def __init__(self, name, age, marks, sex):
        # Inheritence
        super().__init__(name, age, sex)
        self.marks = marks
    
    def display(self):
        super().display()
        print(self.marks)
