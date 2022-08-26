def test1(s):
    for i in range(len(s)):
        if s[i].isalnum():
            return True
    return False
def test2(s):
    for i in range(len(s)):
        if s[i].isalpha():
            return True
    return False
def test3(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True
    return False
def test4(s):
    for i in range(len(s)):
        if s[i].islower():
            return True
    return False
def test5(s):
    for i in range(len(s)):
        if s[i].isupper():
            return True
    return False
if __name__ == '__main__':
    s = input()
    result1 = test1(s)
    result2 = test2(s)
    result3 = test3(s)
    result4 = test4(s)
    result5 = test5(s)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)