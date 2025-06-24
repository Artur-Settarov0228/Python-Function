def is_palindrome(text: str) -> bool:
    if text == text[::-1]:
        return True
    else:
        return False
    
text = input("MAtin kiriting :")
result = is_palindrome(text)
print( result )