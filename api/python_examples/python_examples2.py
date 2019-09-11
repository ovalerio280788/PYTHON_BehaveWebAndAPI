"""
This is an example of classes
"""


class Person:
    def __init__(self, id, name, lastname, gender):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.gender = gender

    @property
    def print_name(self):
        print(self.name)

    @property
    def print_last_name(self):
        print(self.lastname)

    @property
    def print_id(self):
        print(self.id)


class Student(Person):

    def __init__(self, id, name, lastname, gender, card_number):
        super().__init__(id, name, lastname, gender)
        self.card = card_number

    @property
    def print_fullname(self):
        return "{1} {2}, {0}".format(self.id, self.name, self.lastname)

    @staticmethod
    def print_whatever():
        """Static method as an example"""
        print("\n\nWhatever!!")

    @staticmethod
    def multi_return():
        """Multi return method as an example"""
        return 1, 2, 3


students = []
students.append(Student("1", "Oscar", "Valerio", "M", "12345"))
students.append(Student("2", "Oscar2", "Valerio2", "M", "1234567"))
students.append(Student("3", "Oscar3", "Valerio3", "M", "1234589"))

Student.print_whatever()
print(" --> ".join(["{} {}".format(s.name, s.lastname) for s in students]))
print(Student.multi_return())
print(Student.multi_return()[2])
