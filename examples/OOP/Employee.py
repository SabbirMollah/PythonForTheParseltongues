class Employee:
    raise_amount = 1.05
    num_of_emps = 0
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

