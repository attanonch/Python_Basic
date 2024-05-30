#แปลงอุณหภูมิ
temp = input("ป้อนอุณหภูมิ (องศา) : ")#45C
degree = int(temp[:-1]) #ตัวเลข
unit = temp[-1].upper() #หน่วย แปลงเป็นตัวพิมพ์ใหญ่
print(degree,' หน่วย ',unit)

if unit == "C" :
    result =((9*degree)/5)+32
    print("อุณหมูิเป็น",result,"ฟาเรยไฮน์")
elif unit == "F":
    result = (degree-32)*5/9
    print("อุณหมูิเป็น",result,'เซลเซียส')
else :
    print("ลืมเขียนหน่วยมั้ย")

