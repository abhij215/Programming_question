def isPalindrome(str):
    for x in range(int(len(str)/2)):
        if str[x] != str[len(str)-1-x]:
            return False
        return True

a = 'malayalam'
pali = isPalindrome(a)

if pali:
    print('yes')
else:
    print('No')
