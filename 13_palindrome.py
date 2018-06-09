str1 = "abba"


def pal(str1):
    str2 = str1.lower()
    for i in range(len(str2) / 2):
        if str2[i] != str2[len(str2) - i - 1]:
            return False
    return True


print pal(str1)

