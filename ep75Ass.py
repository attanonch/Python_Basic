try:
    # fw=open("Socre.txt","a",encoding="utf8")
    # while True:
    #     studentid=input("ป้อนรหัสนักเรียน : ")
    #     if studentid == "exit" :
    #         break
    #     score=input("ป้อนคะแนนสอบ : ")
    #     fw.writelines(studentid+"\t"+score+"\n")
    # fw.close()
    fr=open("Socre.txt","r",encoding="utf8")
    fa=open("Grad.txt","a",encoding="utf8")
    grade = None
    for line in fr.readlines() :
        score=line[-4:].strip() #คะแนนนักเรียน
        student=line[:-4].strip() #รหัสนักเรียน
        # print("รหัส",student,"คะแนน",score)
        score = int(score)
        if score >= 80 :
            grade = "A"
        elif score >= 70 and score < 80:
            grade = "B"
        elif score >= 50 and score < 69 :
            grade = "C"
        else :
            grade = "F"
        score = str(score)    
        # print("รหัส",student,"คะแนน",score,"เกรดที่ได้ ",grade)

        fa.writelines(student+"\t"+score+"\t"+grade+"\n")
    fr.close()
    fa.close()

except Exception as e :
    print(e)


