def yoshni_hisoblavchi_kankul(tugulgan_yil , hozirgi_yil):
    yosh = hozirgi_yil - tugulgan_yil
    print(f"sizning yoshingiz {yosh} da")

    if yosh >= 18:
        print("balogatga yetgansiz")
    else:
        print("balogatga yetmagansiz")

def main():
    yil = int(input("tugulgan yilingizni kiriting :"))
    hozirgi_yil = int(input("Hozirgi yilingizni kiriting: "))
    yoshni_hisoblavchi_kankul(yil, hozirgi_yil)


main()            