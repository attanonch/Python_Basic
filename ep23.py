#string 
#เข้าถึงผ่าน array โดยใช้ [] แสดงตำแหน่ง
name = 'attanon CHupool 40 ปี 40' #index

# //////////////////////////////

# การเข้าถึงตัวอักษร
# print(name[2]) #t
# print(name[0:3]) #att
# print(name[0:15]) #attanon
print(name[-5:-2])

# print(name[-15:]) #จากหลังมาหน้า
# print("ชื่อว่า "+ name[0:15] ,"อายุ ",name[-2:])


# name2 = name.lstrip() #ช่องวาง ซ้ายขวา strip rstrip lstrip ซ้ายขวา ซ้าน ขวา

# print(len(name2)) #ความบาว string

# print(name.upper()) #ตัวพิมพ์ใหญ่
# print(name.lower())#ตัวพิมพ์เล็ก
# print(name.capitalize()) #ตัวแรกตัวใหญ่

# print(name.replace("40","22",2)) #เปลี่ยนคำ ข้อความเดิม ข้อความใหม่ ตำแหน่งที่จะเปลี่ยน

# x = "attanon" in name #เช็คคำในว่า "ge" ใน name
# if x :
#     name = name.replace("attanon","nattapon")
#     print(name)
# else :
#     pass


# fname = "attanon "
# lname = "chupool "
# age = "22"
# job = "คอม"
# mon = 30000.8888888
# # print("ชื่อ "+fname + " นามสกุล "+ lname ,"อายุ", 22)
# fullname = fname + lname + age
# text = "ชื่อต้น :{}\tนามสกุล :{}\tอายุ :{}\tอาชีพ :{}\t เงินเดือน : {}\t"
# print(text.format(fname,lname,age,'คอม',mon))


# fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุล ข้าวเหนียวทุเรียน ที่ตลาด จะแวะไปสวนทุเรียนด้วย"
# print(fruit.count("ทุเรียน"))

# name = "นายกอไก่ ใจดี"
# num = "1150"
# if name.startswith("นาย") :
#     print(name.startswith("นาย"))
#     print("ถูก")
# else : 
#     print("มั่ว")
# num = "1150"

# if num.endswith("0") :
#     print(num.endswith("0"))
#     print("ถูก")
# else : 
#     print("มั่ว")

# /////////////////////////////
