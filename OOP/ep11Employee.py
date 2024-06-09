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

    def _getincome(self,bonus=0,ot=0):
        return (self.__salary * 12)+bonus+ot

    def __str__(self):
         return f"ชื่อพนักงาน {self._name} แผนก {self.__department} เงินเดือน {self.__salary} รายได้ต่อปี {self._getincome()}"
