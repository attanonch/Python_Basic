#def__str__(self):
class Employee :
    #Class Variable 
    _minSalary = 9000
    __maxSalary = 35000
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

    def _getincome(self):
        return self.__salary * 12

    def __str__(self):
         return print(f"ชื่อพนักงาน {self._name} แผนก {self.__department} เงินเดือน {self.__salary} รายได้ต่อปี {self._getincome()}")

class Accounting(Employee) :
    __departName = "แผนกบัญชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departName)
        super()._showdata()

class Programer(Employee) :
    __departName = "แผนกพัฒนาโปรแกรม"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departName)
        super()._showdata()
class Sale(Employee):
    __departName = "แผนกขายสินค้า"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departName)
        super()._showdata()

account = Accounting("Acc",9000)
# print("รายได้ต่อปี",account._getincome())
programer = Programer("PRO",35000)
# print("รายได้ต่อปี",programer._getincome())
sale = Sale("sales",25000)
# print("รายได้ต่อปี",sale._getincome())
account.__str__()
programer.__str__()
sale.__str__()

# account._showdata()
# programer._showdata()
# sale._showdata()

