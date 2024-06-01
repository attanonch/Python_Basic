data = {"191":"แจ้งเหตุด่วน","1668":"รถโรงพยาบาล","1447":"ดับเพลิง"}

def searchnumber(message) :
    for key, value in data.items() :
        if value == message:
            print("เบอร์ติดต่อ = ",key)
        else : 
            print('ไม่พบข้อมูล ')
            return

message = input("ป้อนข้อมูลที่ต้องการ = ")
searchnumber(message)