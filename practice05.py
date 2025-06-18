def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("tebriklayman siz tugri topdiz")
    else:
        print("Afsuz siz topaolmadiz")

def main():
    secret = 10
    guess = int(input("siz kamp.. ni sirli sonnini kiriting: "))
    result = check_guess(secret ,guess)
    print_result(result) 

main()     