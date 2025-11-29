class Person: # SuperClass/ ParentClass
    def __init__(self, name, age, sex):
        self.name = name    # public
        self._age = age     # protected
        self.__sex = sex    # Private
    
    def display(self):
        print(self.name, self.age, self.__sex)
