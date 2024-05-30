#list คล้ายๆ array

# number = [1,2,3,4,5,6] 
# number = [] #list ว่าง
# name = ["นาย A","นาย B","นาย C "]
# all = ["นายไข่",True,3.14]
# name = list(["นาย A","นาย B","นาย C "]) # constructor

#การแสดงผล
# print(all)

#การเข้าถึงข้อมูล 
# print(number[0]+number[1]).
# print(number[-3:])
# print(number[1:])
# print(name[0],name[1])

# การแก้ไขข้อมูล 
# number = [1,2,3,4,5,6] #list ว่า
# print("ก่อนแก้ไข",number)
# number[0] = 111
# number[-1] = 666
# number[1:] =222,333,444,555,666

# การเข้าถึงสมาชิก loop(
# sum = 0
# number = [1,2,3,4,5,6,7,8,9,]
# for item in number :
#     sum+=item
#     print(item,end="")
# print("\nค่ารวม",sum)

# fruit = ["มะม่วง","มะนาว","มะยม"]

# ตรวจสอบข้อมูล

# if 20 in number :
#     print("เป็น")
# else :
#     print("ไม่เป็น")

# if "มะม่วง" in fruit :
#     print("เป็น")
# else :
#     print("ไม่เป็น")

# number = [1,2,3,4,5,6,7,8,9,]

# การนับจำนวนสมาชิก len  ทำงานร่วมกับ loop
# for i in range(len(number)) :
#     print(number[i])
# for item in number :
#     print(item)

#append นำสมาชิกต่อท้าย
#insert (index,ข้อมูล)ข้อมูลแทรก
# fruit.insert(0,"ส้มโอ")
# fruit = ["มะม่วง","มะนาว","มะยม"]
# number = [1,2,3,4,5,6,7,8,9,]
# print('ก่อนเพิ่ม',fruit)
# fruit.append("มะปราง")
# fruit.append("แตงโม")
# print('หลังเพิ่ม',fruit)
# ลบสมาชิกออก remove
# fruit.remove("มะปราง")
# print("หลังลบ",fruit)

#การลบแบบ pop 
# fruit.pop()
# del fruit[1]
# del fruit #ลบหน่วยความจำไปด้วย
# fruit.clear() # ลบสมาชิกออก
# print("หลังลบ",fruit) 

# การคัดลอกข้อมูล
# fruit = ["มะม่วง","มะนาว","มะยม"]
# number = [1,2,3,4,5,6,7,8,9,]
# x = fruit.copy()
# print(x)
# allGrop = fruit + number
# print(allGrop)
 
# การหาสมาชิก
# number = [1,2,3,4,5,6,7,8,9,1,1,1]
# findone=number.count(1)
# print(findone)

# number = [1,2,3,4,5,6,7,8,9,1,1,1]
# fruit = ["มะม่วง","มะนาว","มะยม"]
# newnum = number.extend(fruit)
# print(number)
# print(newnum)