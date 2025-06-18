def get_grade(score):
    if 90 <= score <=100:
        print("A")
    elif 70 <= score <=80 :
        print("B")
    elif 50 <= score <=60:
        print("C")
    
    else:
        return "natugri ball kiritingiz "
    
def main():
    ball = int(input("ball kiriting :"))
    baho = get_grade(ball)
    print(f"sizning bahongiz {baho}")


main()        
