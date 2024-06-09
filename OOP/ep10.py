#overloading method ข้อมูลมันเกิน
#overriding เรียกใช้function มันเกิน
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

class Accounting(Employee) :
    __departName = "แผนกบัญชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departName)
        self._age = age

    def _showdata(self):
        super()._showdata()
        print("อายุ ".format(self._age))

    def __str__(self):
        # return (super().__str__()+" , อายุ {} ปี".format(self._age))
        # return (super().__str__()+" , อายุ = {} ปี".format(self._age))
        return super().__str__() + f" , อายุ = {self._age} ปี"

class Programer(Employee) :
    __departName = "แผนกพัฒนาโปรแกรม"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departName)
        self.experience = experience
        self.skill = skill

    def _showdata(self):
        super()._showdata()
        print("ประสบการณ์ {}".format(self.experience))
        print("ความสามารถ {}".format(self.skill))

    def __str__(self):
        # return (super().__str__() + " , ประสบการณ์ {} ปี, ความสามารถ {}".format(self.experience,self.skill))
        # return (super().__str__()+" , ประสบการณ์ = {} ปี, ทักษะ = {}".format(self.experience,self.skill))
        return super().__str__() + f" , ประสบการณ์ = {self.experience} ปี, ทักษะ = {self.skill}"
        

class Sale(Employee):
    __departName = "แผนกขายสินค้า"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departName)
        self.area = area
    def _showdata(self):
        super()._showdata()
        print("พื้นที่ {}".format(self.area))
    def __str__(self):
        # return (super().__str__()+" , พื้นที่จังหวัด {}".format(self.area))
        # return (super().__str__()+" , พื้นที่รับผิดชอบ = {}".format(self.area))
        return super().__str__() + f" , พื้นที่รับผิดชอบ = {self.area}"
        

account = Accounting("Acc",9000,22)
programer = Programer("PRO",35000,3,"PYTHON")
sale = Sale("sales",25000,"BKK")
print(account._getincome(500,6000))
# account._showdata()
# programer._showdata()
# sale._showdata()
# print(account.__str__())
# print(programer.__str__())
# print(sale.__str__())





