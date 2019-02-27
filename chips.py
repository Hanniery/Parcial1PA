if __name__ == '__main__':
    numbers = input()
    n, m, i = int(numbers.split(' ')[0]), int(numbers.split(' ')[1]), 1
    
    while(i <= n and m >= i):
        m -= i
        i += 1
        if i > n:
            i = 1

    print(m)
