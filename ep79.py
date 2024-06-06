#Module Data
import datetime

result=datetime.datetime.now() #ดึงเวลาปัจจุบัน
# print(result.year) #ปี
# print(result.month) #เดือน
newtime = datetime.datetime(2020,6,20) #yyyy,mm,dd
# print(newtime)


#รูปแบบแสดงผล

print("เริ่มต้น :",result)
print("ปรับ :",result.strftime("%x")) #m/d/y
print("ปรับ :",result.strftime("%X")) #เวลา
print("ปรับ :",result.strftime("%c")) #วัน จันทร์

#เวลา
print("ปรับ :",result.strftime("%H:%M:%S %p"))

#1-366
print(result.strftime("%j")) #ลำดับวัน

# date
print(result.strftime("%a")) #แบบสั้น
print(result.strftime("%A")) #แบบยาว
print(result.strftime("%w")) #0 =sunday
print(result.strftime("%d")) #วันที่
print(result.strftime("%b")) #เดือนแบบสั้น
print(result.strftime("%B")) #เดือนแบบเต็ม
# วดป
print(result.strftime("%d /%m /%Y"))

