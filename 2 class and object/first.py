class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setEmpid(self,empid):
        self.empid=empid
    def setName(self,name):
        self.name=name
    def setSalary(self,salary):
        self.salary=salary
    def getEmpid(self):
        return self.empid
    def getName(self):
        return self.name
    def getsalary(self):
        return self.salary
     
e1=Employee()
e2=Employee(101,"Rahul",20000)
e1.setEmpid(105)
e1.setName("Abhisek")
e1.setSalary(25000.00)
print(e1.getEmpid(),e1.getName(),e1.getsalary())
print(e2.getEmpid(),e2.getName(),e2.getsalary())