def add(a,b ):
    result = a + b
    return result

def subtract(a,b):
    result = a - b
    return result

def multiply(a,b):
    result = a * b
    return result
def divide(a,b):
    result = a / b
    return result

def main():
    a = int(input("a = "))
    b = int(input("b = "))
    op = input("+, - , * , / =")
    if op =="+":
       print( add(a,b) )
    elif op =="-":
       print( subtract(a,b) )
    elif op =="*":
        print(multiply(a,b))

    elif op =="/":
        print(divide(a,b))
    else:
        print("error")

main()