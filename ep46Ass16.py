#การค้นหาและนับจำนวนตัวอักษรในสมาชิก
message = ["aa","aab","cba","bba","abb","cca","aaaaaaaaaaaaa"]
result = []
for item in message:
    result.append(item.count("a"))
print(result)