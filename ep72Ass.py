#โปรแกรมบัญชีธนาคาร

# data
account = {"นายA":5000,"นายB":0}

def getBalance():
    print('ยอดเงินคงเหลือในบัญชี : ',account)

def deposit(money) :
    if money <= 0 :
        raise Exception ("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    print("ฝากเงินเข้าบัญชี A :",money)
    account["นายA"]+=money

def withdraw(money) :
    if money <= 0 :
        raise Exception ("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money > account["นายA"] :
        raise Exception ("ยอดเงินมีไม่เพียงพอ")
    print("ถอนเงินจากบัญชี A: ",money)
    account["นายA"]-=money

def tranfer(money) :
    if not type(money) is int and not type(money) is float:
        raise Exception('ต้องป้อนตัวเลขเท่านั้น')
    if money <= 0 :
        raise Exception ("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money > account["นายA"] :
        raise Exception ("ยอดเงินมีไม่เพียงพอ")
    print("ทำการโอนเงินจากบัญชี A ไปบัญชี B : ",money)
    account["นายA"]-=money
    account["นายB"]+=money

try :
    getBalance()
    tranfer(300.50)
    getBalance()
except Exception as e :
    print(e)
