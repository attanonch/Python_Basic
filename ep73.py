# อ่านไฟล์
#  open("ชื่อไฟล์","โหมด","เข้ารหัส")

t = open("ep73.txt","r",encoding="utf8")
print(t.read())

try :
    t = open("ep753.txt","r",encoding="utf8")
    print(t.read())
except FileNotFoundError:
    print("หาไฟล์ไม่เจอ")