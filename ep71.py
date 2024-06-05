#Exception
'''
try:
    คำสั่งรันโปรแกรมปกติ
except:

'''

# ValueError => ค่าผิดพลาด
# ZeroDivisionError  /0
while True :
    try:
        name = input("กรอกชื่อ ")
        num1 = int(input("กรอกตัวเลข 1 : ")) 
        num2 = int(input("กรอกตัวเลข 2 : ")) 
        if num1==0 and num2==0 :
            break 
        if num1 < 0 or num2 < 0:
            raise Exception("ไม่สามารถป้อนค่าติดลบได้นะครับ")
        if name == "non" :
            raise Exception("ถูกแบน")
        result = num1/num2
        print(result)
        # score = 100+"50"
        # print(score)
    except Exception as e :
        print(e)
    else :
        print("ทำอะไรต่อ")
    finally:
        print("จบโปรแกรม")

# except ValueError:
#     print("ต้องป้อนตัวเลขเท่านั้น")
#     pass
# except ZeroDivisionError:
#     print("ห้ามหารด้วยเลขศูนย์นะครับ")
#     pass
# except TypeError:
#     print("ชนิดข้อมูลไม่ตรงกัน")
#     pass



