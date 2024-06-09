#Inheritance
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


class Accounting(Employee) :
    __departName = "แผนกบัญชี"
    def __init__(self):
        pass
class Programer(Employee) :
    __departName = "แผนกพัฒนาโปรแกรม"
    def __init__(self):
        pass
class Sale(Employee):
    __departName = "แผนกขายสินค้า"
    def __init__(self):
        pass

account = Accounting()
# print(account._Employee__maxSalary)  #กรณีตั้งเป็น private 
programer = Programer()
print(account._minSalary)
salr = Sale()
print(account._commanyname)
