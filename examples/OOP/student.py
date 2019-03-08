class Student:
    MIN_CGPA = 0
    MAX_CGPA = 4.0
    PROBATION_LIMIT = 2.0
    _money_amount = 0
    def __init__(self, first, last, cgpa, id):
        self.first = first 
        self.last = last
        self.cgpa = cgpa
        self.id = id

    def greet(self):
        print("Hello World!")

    def add_course(self):
        if(self._money_amount < 16000):
            print("You can't add course")
        else:
            print("Succesful")
            self._money_amount -= 16000

    def add_money(self, amount):
        self._money_amount += amount