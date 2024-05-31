# dictionary => key,value
# การสร้าง
# ชื่อตัวแปร = {key:value,key:value}


lis = ["แดง","เหลือง","เขียว"]
tup = ("แดง","เหลือง","เขียว")
s = {"แดง","เหลือง","เขียว"}

# ประกาศแบบปกติ
# print(lis)
colors = {"red":'แดง',"green":"เขียว",'black':'ดำ',98:"บ้านแสนสุข",100:"บ้านป่า",True:"ถูก"}
# city = {"bankok":"กรุงเทพ"}
# anime = {'ไก่':"chicken","แมว":"cat"}
# room = {100:"นนท์",200:"นาย B"}
# print(city["bankok"])
# print(room[200])

# ประกาศแบบ consture
animals = dict(cat="แมว",dog="หมา")
# print(animals["cat"])
# print(animals.get("dog"))
# print(colors.get(True))

#เพิ่มค่าโดยการ update กรณี key ซ้ำ จะทำการ update 
# colors.update({"pink":"ชมพู"})
# print(colors)

# ดึงข้อมูลแต่ละตัว  .key() .value() .item()
# for i,j in colors.items() :
#     print("key: ",i,"value => ",j)

# print("ก่อน",colors)
# colors.pop("red") #ลบข้อมูล
# colors.popitem() #ข้อมูลท้ายสุดดดดดดดดด
# colors.clear() #ลบข้อมูลทั้งหมด
# del colors # ลบจากหน่วยความจำ

# การคัดลอกตัวแปร 
# x = colors.copy()
# print(x)

market = {
    "ร้านป้าพร" : {
        "name" : "ป้าพร",
        "menu" : ["กะเพราะไก่", "ก๋วยเตี๋ยว"],
        "zome" : 'ตะวันออก'
    },
    "ร้านลุงป้อม" : {
        "name" : "น้าจ๊อบ",
        "menu" : ["มะม่วง", "ทุเรียน"],
        "zome" : 'ทางเข้าตลาด'
    },
    "ร้านน้าใจ" : {
        "name" : "น้าใจ",
        "menu" : ["นมเย็น", "ชาเย็น"],
        "zome" : 'ทางออก'
    },
}
print(market["ร้านน้าใจ"]["menu"])