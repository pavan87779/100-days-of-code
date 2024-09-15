class Myclass:
    x=5

p1=Myclass()
#print(p1.x)
p1.x=10
#print(p1.x)
#__init__()
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def myfunc(self):
        print("Hello my name is "+self.name)
        return


p1=person("jhon",36)
del p1.age
p1.age=40

print(p1.name, "\n",p1.age)
#print(p1)
print(p1.myfunc())

#Inheritance
#childclass
class Student(person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)



