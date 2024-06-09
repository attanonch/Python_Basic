from ep11Employee import Employee
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