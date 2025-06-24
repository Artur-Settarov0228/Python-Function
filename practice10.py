def is_strong_password(password: str) -> bool:
    count = 0
    for i in password:
        count += 1
        return count > 8
    
pasword = float(input("paril kiriting :"))
reulst = is_strong_password(pasword)
print(reulst)    