
#Get 
#Set  
class Employee :
    def __init__(self,name,salary,department) :
        
        # protected attribute
        self._name = name # _ = protect
        self.__salary = salary # __ = private
        self.__department = department # __ = private
        
    def _showdata(self) : #protected methon
        print(f'ชื่อว่า {self.getName()}')
        print(f'เงินเดือน {self.getSalary()}')
        print(f'อาชีพ {self.getSalary()}')
       
    #setter method 
    def setName(self,newname) :
        self._name = newname

    def setSalary(self,newsalary) :
        self.__salary = newsalary
    
    def setDepartment(self,department) :
        self.__department = department

    #getter method
    def getName(self) :
        return self._name
    
    def getSalary(self) :
        return self.__salary
    
    def getDepartment(self) :
        return self.__department

obj1 = Employee("นนท์",50000,"โปรแกรมเมอร์")
# print(f"พนักงานดีเด่น คือ {obj1.getName()}")
# print("พนักงานดีเด่น คือ {}".format(obj1.getName()))
# print("รายได้คือ คือ {}".format(obj1.getSalary()))
# print("แผนก คือ {}".format(obj1.getDepartment()))
obj1._showdata()


# obj1.setName("ATTANON")
# obj1.setSalary(70000)
# obj1.setDepartment("นักวิชาการ")
# obj1._showdata()