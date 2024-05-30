#BMI 

w = int(input("input weight : "))
h = int(input("input high : ")) / 100
bmi = w/(h*h)

if(bmi < 18) :
    print("ค่าBMI ",bmi," ต่ำกว่าเกณฑ์")
elif 18.5<bmi<22.9 :
    print("ค่าBMI ",bmi," สมส่วน")
elif 23<bmi<24.9 :
    print("ค่าBMI ",bmi," น้ำหนักเกิน")    
elif 25<bmi<29.9 :
    print("ค่าBMI ",bmi," โรคอ้สนระดับที่ 1")
else :
    print("ค่าBMI ",bmi," โรคอ้วนระดับอันตราย")
