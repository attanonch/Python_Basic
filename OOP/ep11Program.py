from ep11Accounting import Accounting
from ep11Programer import Programer
from ep11Sale import Sale

account = Accounting("Acc",9000,22)
programer = Programer("PRO",35000,3,"PYTHON")
sale = Sale("sales",25000,"BKK")

print(account.__str__())
print(programer.__str__())
print(sale.__str__())