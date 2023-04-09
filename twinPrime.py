def twinPrime(num):
    if num < 3 and num > 0:
        print(0)
    if num < 0:
        print(-1)
    if num > 3:
        for i in range(num-1):
            if isPrime(i) and isPrime(i+2):
                print((i,i+2))

def isPrime(test):
    for i in range(2, test):
        if test % i == 0:
            False
            break
    else:
        return True

if __name__ == '__main__':
    inputString = input()
    inputNumber = int(inputString)
    twinPrime(inputNumber)