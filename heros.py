if __name__ == '__main__':
    s, t = input(), input()
    vocales, output, i = 'aeiou', 'NO', 0

    while(len(s) == len(t) and i < len(s)):
        output = 'YES'
        vocal_s = s[i] in vocales
        vocal_t = t[i] in vocales
        if vocal_s != vocal_t:
            output = 'NO'
            break
        i += 1
            
    print(output)
