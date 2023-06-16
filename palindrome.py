def polindrome(s):
    return s == s[::-1]

while True:
    s = input('введите слово полиндром без пробелом в нижнем регистре\n ')
    if polindrome(s):
        print('True')
    else:
        print('False')

