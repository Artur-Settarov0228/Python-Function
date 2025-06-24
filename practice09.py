
def deposit(balance, amount):
    balance += amount
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print("mablag yetarli emas")
    else:
        balance -= amount
        return balance
    
def check_balance(balance) :
    print(f"sizni pilingiz {balance} som qoldi")   


   
balance = int(input("balanc = "))
amount = int(input("amount = "))



result = int(input("---Amalni tanlang---""\n"
               "1.Balansga pul qo'shish""\n"
               "2.Balansdan pul ayirish "))

if result == 1:
    natija = deposit(balance,amount)
elif result == 2:
    natija = withdraw(balance,amount)

print(natija)