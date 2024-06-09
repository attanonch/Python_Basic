from ep11Employee import Employee

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