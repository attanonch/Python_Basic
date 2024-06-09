from ep11Employee import Employee

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