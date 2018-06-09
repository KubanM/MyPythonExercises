
def isPalindrome(str):
    if len(str) > 0:
        for i in range(len(str) / 2):
            if str[i] != str[len(str) - i - 1]:
                return False
        return True
    return "Empty string"


aa = 'abba'
print isPalindrome(aa)

