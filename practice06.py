def is_valid_phone_number(phone: str):
    return phone.isdigit() and len(phone) == 9

def main():
    tel = (input("raqam kirirng:"))
    if is_valid_phone_number(tel):
        print("siz tugri raqam kiritdiz")
    else:
        print("siz tarmoqda mavjutmas raqam kiritingiz")


main()        