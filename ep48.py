#list = ข้อมมูลต่างกันได้ , แก้ไขข้อมูลได้, ข้อมูลซ้ำกันได้, ซ้ายไปขวา
#tuple = ข้อมมูลต่างกันได้ , แก้ไขข้อมูลไม่ได้, ข้อมูลซ้ำกันได้, ซ้ายไปขวา
#set = ข้อมมูลต่างกันได้ , แก้ไขข้อมูลสมาชิกได้, ข้อมูลซ้ำกันไม่ได้, ลำดับไม่แน่นอน

#แบบปกติ
fruit = {"มะม่วง","มะขาม","มะยม","มะยม"}
# constructor
# name = set(["attanon","chupool"])

# เพิ่มข้อมูลสมาชิก
# fruit.add("ทุเรียน")
# fruit.add("สับประรด")
# fruit.add("999")

# เพิ่มสมาชิกหลายตัว
# lis = ["ตะไคร้","ชะอม"]
# fruit.update(lis)

# แสดงผล
# for input in fruit :
#     print("ข้อมูล " , input)

# นับจำนวนใช้ len 

# หา สมาชิก
# if "ทุเรียน" in fruit :
#     print("มี")
# else :
#     print("ไม่มี")

# ลบข้อมูล 
# fruit.remove("มะขาม")  #ถ้าไม่เจอข้อมูล จะ error
# fruit.discard()   #ลบแบบถ้าไม่เจอข้อมูล จะไม่error
# fruit.clear() เป็นการลบข้อมูลใน
# del fruit ลบทั้ง memmory

print(fruit, type(fruit),len(fruit))
