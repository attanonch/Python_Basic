'''
# constructor = เป็นพิเศษที่ถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ

def __init__(self) :
    pass

#destructor = จะถึงเรียกใช้งานเมื่อสิ้นสุดวัตถุ
def __del__(self) :
    pass
     
'''
# การสร้าง Constructor

# create class
class Employee:

    def __init__(self,name,salary,department) :
        print("Default Construtor")
        self.name = name
        self.salary = salary
        self.department = department
    # method
    def showdata(self) :
        print("ชื่อพนักงงาน = {}".format(self.name))
        print(f"เงินเดือน = {self.salary}")
        print(f"ตำแหน่ง {self.department}")

    def __del__(self):
        print("Call Destructor")
        
# create object
obj1 = Employee("นนท์ ",50000,"บัญชี")
obj1.salary = 70000
obj1.showdata()

obj2 = Employee("non",30000,"โปรแกรมเมอร์")
obj2.name= "NONONONONONONON"
obj2.showdata()

obj3 = Employee("nat",790000,"โปรแกรมเมอร์")
obj3.showdata()






