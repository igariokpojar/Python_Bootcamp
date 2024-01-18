class Person:  # On these Classes we crate multilevel Inheritance
    def __init__(self, name: str, age: int):  # this is the constructor
        self.name = name
        self.age = age

    def __str__(self):  # toString method to print in the Console
        return f'{type(self).__name__}{self.__dict__}'


class Employee(Person):  # Python support multiple Inheritance and NO Interface

    def __init__(self, name: str, age: int, job_title: str, company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age)  # calling parent class' constructor
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')


class Developer(Employee):

    def work(self):
        print(f'{self.job_title} {self.name} is coding')


class Teacher(Employee):

    def __init__(self, name: str, age: int, job_title: str = "Teacher", company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age, job_title, company_name, salary)  # calling parent class' constructor

    def work(self):
        print(f'{self.name} is teaching Nursing Program')


employee1 = Employee('Alex', 7, 'QA', 'Apple Inc', 150_000)

developer1 = Developer('Igariok', 40, 'Python Developer', 'Google Inc', 128_000)

teacher = Teacher('Alla', 45, 'RN', 'Advocate Sherman', 185_000)

print(employee1)  # we call ToString
print(developer1)
print(teacher)

employee1.work()  # here we call the method form this class
developer1.work()
teacher.work()
