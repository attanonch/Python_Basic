#list เปลี่ยนแปลงได้
#tuple ข้อมูลสมาชิก เปลี่ยนแปลงไม่ได้

# b=tuple((1,2,3,"attanon",True))
# a=list([1,2,3])

# tup = (1,2,3,"attanon",True,3.99) #เหมือน list แต่เปลี่ยนค่าไม่ได้ สลับตำแหน่งไม่ได้
# lis = [1,2,3,"attanon",True]

# lis[0] = "999"

# print(tup[-3:0])#ตัวสุดท้าย -1 ตัวแรก เรริ่มที่ 0 
# print(lis)a

# tup = (1,2,3,"attanon",True,3.99) #เหมือน list แต่เปลี่ยนค่าไม่ได้ สลับตำแหน่งไม่ได้
# #แก้ไข tup โดยการแปลงเป็น list 
# list = list(tup)
# print("ก่อน",tup,type(tup))
# print("ก่อน",list,type(list))
# list[0] = 999
# tup = tuple(list)
# print("หลัง",tup,type(tup))
# print("หลัง",list,type(list))

# tup = (1,2,3,"attanon",True,3.99) 

# วนลูป

# for item in tup :
#     print(item,end=" ")

# if "attanon" in tup:
#     print("มี")
# else :
#     print("ไม่มี")

# จำนวน
# print(len(tup))

# for i in range(len(tup)) :
#     print(tup[i],end=" ")

# สร้าง tuple  เพิ่มข้อมูลใน tuple การจอย  tupple 
# name = ("attanon","somphak")
# new = ("nat","ann")
# allname = name+new
# print(allname)


# tup = (1,2,3,"attanon",True,3.99)
# city = ["กรุงเทพ",'นคร',"ชลบุรี"]

# tup = tup+tuple(city)
# print(tup)

# การใช้ del 

# tup = (1,2,3,"attanon",True,3.99)
# list = list(tup)
# print("befor",list)
# list.pop()
# list.remove(1)
# print("After",list,type(list))
# tup = tuple(list)
# print(tup,type(tup))

# หา count
# tup = (1,2,3,"attanon",True,3.99,4,4,4,4,)
# tup.count(4)
# print(tup.count(4))

# หา index ที่เจอเลข
# tup = (1,2,3,"attanon",True,3.99,4,4,4,4,)
# print(tup.index("attanon"))
# tup = (11,2,3,55,43,48,42,43,)
# lis = list(tup)
# lis.sort()
# lis.reverse()

# tup = tuple(lis)
# print(tup,type(tup))

# tup = (10,20,30)
# x,y,z = tup

# character = ("a",'t',"t",'a','n','o','n')
# name = ''.join(character)
# print(name)