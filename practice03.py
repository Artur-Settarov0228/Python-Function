def is_even(numer):
    return numer % 2 ==0
def is_even_chiqar(numer):
    if is_even(numer):
        print(f"{numer} - juft son")
    else:
        print(f"{numer} - toq son")

def main():
    numer = int(input("son kiriting :"))
    is_even_chiqar(numer) 


main()           