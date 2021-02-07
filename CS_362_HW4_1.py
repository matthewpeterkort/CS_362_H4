def cubevolume(length):
    length=input("Enter the side length of the cube in inches")
    length=int(length)*int(length)*int(length)
    length=int(length)
    print("The volume of the cube is",length,"cubic inches")
    return length

def average():
    array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    return sum(array)/len(array)
def name():
    FN=input("Enter a first name")
    LN=input("Enter a last name")
    return FN+LN
