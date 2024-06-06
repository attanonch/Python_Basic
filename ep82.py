# รหัส 
import random

atmpass = "1"
result= '' #เก็บผลลัพธ์


list_num=random.choice("0123456789")
print(list_num)

while result!= atmpass :
    result = ''
    for letter in range(len(atmpass)):
        list_num=random.choice("0123456789")
        result=''.join(list_num)+str(result)
        print("SEARCH = ",result)
print("CREAK PASSWORD IS ",result)