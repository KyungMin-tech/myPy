# 큐와 스택을 사용하지 않고 회문 찾기

def palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i].isalpha() == False:
            i += 1
        elif s[j].isalpha() == False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1

    return True
        
 

print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam"))
