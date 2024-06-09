
#Class Variable เปรียบเสมือน Global Variable
#Instance Variable ใช้ได้เฉพาะ Class 
class Employee :
    #Class Variable 
    _minSalary = "9000"
    _maxSalary = "35000"
    _commanyname = "ATTANON COMPANY"

    def __init__(self,name,salary,department) :
        
        # Instance Variable
        self._name = name # _ = protect
        self.__salary = salary # __ = private
        self.__department = department # __ = private
        
    def _showdata(self) : #protected methon
        print(f'ชื่อว่า {self._name}')
        print(f'เงินเดือน {self.__salary}')
        print(f'อาชีพ {self.__department}')
       

obj1 = Employee("นนท์",50000,"โปรแกรมเมอร์")
print(Employee._minSalary) #ไม่ต้องสร้าง class
print(Employee._maxSalary) #ไม่ต้องสร้าง class
print(Employee._commanyname) #ไม่ต้องสร้าง class
print(obj1._name)
# obj1._showdata()

#ถ้าเป็น ไม่เป็น function ไม่ต้อง () 
#ถ้าเป็น function ให้เติม ()