'''
โครงสร้างควบคุม
1.ลำดับ
2.แบบเลือก
3.แบบทำซ้ำ

if(เงื่อนไขเป็นจริง):
    ย่อหน้า
เช็คทุค เงื่อนไช
'''
age = int(input("กรุณากรอกอายุ :"))


if age >= 15 and age < 20 :
    print("นาย นางสาว")
elif age >= 20 and age < 30:
    print("ผู้ใหญ่")
elif age >= 30:
    print("ทำงาน")
else :
    print("มั่วละ")
    
print("จบโปรแกรม")


