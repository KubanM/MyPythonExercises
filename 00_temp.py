
def isPalindrome(str):
    for i in range(len(str) / 2):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


aa = ''
print isPalindrome(aa)
