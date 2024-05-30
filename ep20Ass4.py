#แยกธนาบัตร

number = int(input("กรอกเงิน "))



if number>=1000 :
    print("1000 บาท ",int(number/1000),'ใบ')
    number = number % 1000
    
if number>=500 :
    print("500 บาท ",int(number/500),'ใบ')
    number = number % 500
    
if number>=100 :
    print("100 บาท ",int(number/100),'ใบ')
    number = number % 100

if number>=50 :
    print("50 บาท ",int(number/50),'ใบ')
    number = number % 50

if number>=20 :
    print("20 บาท ",int(number/20),'ใบ')
    number = number %20
