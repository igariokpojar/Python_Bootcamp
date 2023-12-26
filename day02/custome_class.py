import numbers


class Employee:  # in Python, we create a class ONLY to create the Objects

    is_human = True  # similar to static variable of Java
    planet = 'Earth'

    def __init__(self, name: str = 'Unknown', job_title: str = 'Java Developer', salary: numbers = 0):
        # __init__ -> constructor used to initialize the attributes
        # also declare Instance (Objects) variables
        self.name = name  # SELF or (this. in Java) keyword is used to call the Instance variable
        self.job_title = job_title
        self.salary = salary

    def work(self):  # this is a Method not a (Function -> is defined out of the Class)
        # to access the method (WORK) we need to call though the Object ONLY
        print(f'{self.name} is working as {self.job_title}')

    def __str__(self):  # To String method in Java
        return f'{type(self).__name__}{self.__dict__}'
    #  __dict__ -> means Dictionary of this Class (all fields)

    #  __name -> private access modifier
    #  _name -> protected access modifier / we can achieve through Inheritance


employee1 = Employee()  # Create Employee Objects

print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee('Alexandru', 'Java Software Engineer', 185000)

print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

employee3 = Employee('Meda', 'Google Software Engineer', 155000)

print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

employee4 = Employee('Igor', 'Python Developer', 150_000)
print(employee4.name)
print(employee4.job_title)
print(employee4.salary)

# print(Employee.name)
print(Employee.is_human)  # access the static variable through the class
print(Employee.planet)

employee1.work()  # to access the method (WORK) we need to call though the Object ONLY
employee2.work()
employee3.work()
employee4.work()

print(employee1)
print(employee2)
print(employee3)
print(employee4)
