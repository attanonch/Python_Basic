#หาจำนวนตัวอักษรพิมพ์เล็กกี่ตัว/พิมพ์ใหญ่กี่ตัว

def checkstring(message) :
    result={"upper":0,"lower":0}
    for c in message :
        if c.isupper() :
            result["upper"]+=1
        elif c.islower() :
            result["lower"]+=1
        else :
            pass
    return result

message=input("input your message :")
x=checkstring(message)
print(x)



