def average():
    array=[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]
    return array

def factorial(number):
    if (number==1):
        return 1
    number=number-1
    return number*factorial(number-1);
