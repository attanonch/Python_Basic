#Recursive Function ฟังก์ชันเรียกตัวเอง 
'''
หาจุดวนซ้ำ
หาจุดออกจาก function
ต้องมี parameter
'''

# def count(a) :
#     if  a == 5:
#         return
#     print(a)
#     a+=1
#     count(a)
  
def summation(number) :
    if number == 1 :
        return number
    else :
        return number + summation(number-1)

x = summation(5)

print(x)