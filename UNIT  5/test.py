class Person: #the parent class
    #assing attributes
    def __int__(self,name,age,cid):
        self.name = name
        self.age = age
        self.cid = cid

#defioning behaviour 
def walk(self):
    print(self.name, "is walking")
def talk(self):
    print(self.name, "is talking")
def sleep(self):
    print(self.name, "is sleeping")
def eat(self):
    print(self.name, "is eating")  

class Teacher(Person):
    def __int__(self,name, age, cid, subject, salary, department, designation):
        super().__init__(name,age,cid)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.desgination = designation

def teach(self):
    print(self.name, "is teaching")
def grade_students(self):
    print(self.name, "is grading")
def attend_meeting(self):
    print(self.name, "is attending the meeting")

class Student(Teacher):
    def __int__(self, name, age, cid, std_id, course, year, gpa):
        return super().__int__(name, age, cid)
        self.std_id = std_id
        self.course = course
        self.year = year
        self.gpa = gpa

def study(self):
    print(self.name, "is studying")
def attend_class(self):
    print(self.name, "is attending the class")
def write_exam(self):
    print(self.name, "is attending the EXam")   


t1 = Teacher("tashi",30,11111,"BIA",60000,"SCI","Samtse")
t2 = Teacher("dorji",31,22222,"MGT",70000,"ENG","MOngar")

s1 = Student("Kan",18,1111,12345,"BBI",1,3.2)
s2 = Student("Jan",19,333,4321,"BBM",3,3.3)


    