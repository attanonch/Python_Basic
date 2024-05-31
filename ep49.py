#set
# fruitA = {"กล้วย","มะยม","มะนาว","ทุเรียน","ส้มโอ"}
# fruitB = {"ส้มโอ","กีวี","มะม่วง"}

# union and copy ทั้ง A และ B 
# allFruit = fruitA.union(fruitB)
# fruitA.update(fruitB)
# fruitC=fruitA.copy()

#diffrence - 
# fruitC = fruitA.difference(fruitB)

#intersection ตัวซ้ำ
# fruitC = fruitA.intersection(fruitB)
# print(fruitC)

# subset ค่าสูงสุด ค่าตำสุด
# num = {1,2,3,4,5,6,7,8,9,99,88,77,66,55,4,44,22,33}
# print(min(num))
# print(max(num))


#frozenset เปลี่ยนแปลงอะไรไม่ได้
tel = frozenset([1,2,3])

for i in tel :
    print(i)