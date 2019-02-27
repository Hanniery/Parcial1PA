if __name__ == '__main__':
    number = int(input())

    while(number != 0):

        factorial = 1
        for i in range(1, number + 1):
            factorial *= i

        suma_factorial = 0
        for numb in str(factorial):
            suma_factorial += int(numb)

        print(suma_factorial)
        number = int(input())
