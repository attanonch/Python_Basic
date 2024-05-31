# parameter ที่ไม่สามารถระบุค่าได้ *agrs มีลักษณะเป็น Tuple
# ต้องมี * ที่พารามิเตอร์ 

def add(*agrs) :
    sum = 0
    # for item in agrs :
    #     sum +=item

    for i in range(len(agrs)) :
        sum +=agrs[i]
    print("ผลรวม", sum)

# def add(x,y):
#     print(x+y)
# def addthree(x,y,z):
#     print(x+y+z)

# addthree(5,10,15)

add(1,2,3,4,5,6,7,8,9,10)