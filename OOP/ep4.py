#Encapsulation 
# _ = protect
# __ = private
# ว่างๆ = public 
class Employee :
    def __init__(self,name,salary,department) :
        # public attribute
        # protected attribute
        self._name = name # _ = protect
        self.__salary = salary # __ = private
        self.__department = department # __ = private
        
        
    # protect method
    def _showdata(self) : #protected methon
        print(f'ชื่อว่า {self._name}')
        print(f'เงินเดือน {self.__salary}')
        print(f'อาชีพ {self.__department}')

    
obj1 = Employee("นนท์",50000,"โปรแกรมเมอร์")
# obj1.name = "NON"
obj1._name = "NON"
obj1.__salary = 70000
obj1._showdata()

'''
public = เข้าถึงได้มั้ย
protected_ = เข้าถึงได้เฉาะ ใน class obj ตัวสืบทอด
private__ = เข้าถึงแค่ใน class 

'''