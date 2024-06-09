# ชื่อ , เงินเดือน

# create class


class Employee:
    # method
    def detail(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
    def showdata(self) :
        print("ชื่อพนักงงาน = {}".format(self.name))
        print(f"เงินเดือน = {self.salary}")
        print(f"ตำแหน่ง {self.department}")

# create object
obj1 = Employee()
obj1.detail("นนท์",50000,"บัญชี")
obj1.showdata()

obj2 = Employee()
obj2.detail("non",30000,"โปรแกรมเมอร์")
obj2.showdata()

obj3 = Employee()
obj3.detail("nat",790000,"โปรแกรมเมอร์")
obj3.showdata()




