# function เรียกใช้ function

def comparethree(x,y,z) :
    return comparetwo(comparetwo(x,y),z)
    



def comparetwo(a,b) :
    if a < b :
        return b
    else : 
        return a
    
max = comparethree(10,115,50)
print(max)