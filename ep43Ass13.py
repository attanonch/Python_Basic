#การหาค่ายกกำลังของแต่ละ listื
number = [1,2,3,4,5,6,7,8,9]

#ปกติ
# for i in number :
#     pow = i*i
#     print(pow,end=" ")

#ปกติ

# for i in range(len(number)) :
#     number[i] = number[i]**2
# print(number)

#ลดรููป
number = [i*i for i  in number]
print("ลดรูป",number)