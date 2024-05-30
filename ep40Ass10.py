#หาคู่ หาคี่ 
num = [] 
odd = [] #เลขคี่
even = [] #เลขคู่



while True :
    x = int(input("ป้อนค่า :"))
    if x < 0 :
        break
    if x % 2 == 0 :
        even.append(x)
    else :
        odd.append(x)
    num.append(x)

print(num)
print("เลขคู่ ",even)
print("เลขคี่ ",odd)