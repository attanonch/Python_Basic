#  ฟังก์ชันเสริม
#  isinstance เช็คว่า obj สร้างจาก class นั้นมั้ย
#  dir รายชื่อ metyhod ที่สามารถใช้งานได้
class Employee :
    def __init__(self,name,salary,department) :
        self.name = name
        self.salary = salary
        self.department = department
    def showdata(self) :
        print(f'ชื่อว่า {self.name}')
        print(f'เงินเดือน {self.salary}')
        print(f'อาชีพ {self.department}')
    def __del__(self):
        pass
obj1 = Employee("นนท์",50000,"โปรแกรมเมอร์")
obj2 = Employee("นนท์",50000,"โปรแกรมเมอร์")
obj3 = Employee("นนท์",50000,"โปรแกรมเมอร์")

# print(isinstance(obj1,Employee))
# print(dir(obj1))
# print(obj1.__class__) #เชค็ว่าสร้างมาจาก class อะไร
