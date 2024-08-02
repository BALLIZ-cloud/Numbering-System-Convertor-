"""
TA:NOUR KHALID
mohand salah tamer badawy 20231182
ahmed hatem tawfik abdullah 20231007
mohamed gamal zeinhom ali 20230326
"""
# change number from decimal to decimal
def dec_to_dec(num):
    return num


# change number from hexadecimal to hexadecimal
def hexa_to_hexa(num):
    return num


# change number from octal to octal
def octal_to_octal(num):
    return num


# change number from binary to binary
def bin_to_bin(num):
    return num


# change number from binary to hexadecimal
def bin_to_hexa(num):
    binint = int(num)
    dec = 0
    i = 0
    while binint > 0:
        dec += binint % 10 * (2 ** i)
        binint = binint // 10
        i += 1
    num = dec
    digits = "0123456789ABCDEF"
    x = (num % 16)
    rest = num // 16
    if (rest == 0):
        return digits[x]
    else:
        return dec_to_hexa(rest) + digits[x]


# change number from binary to octal
def bin_to_octal(num):
    binint = int(num)
    dec = 0
    i = 0
    while binint > 0:
        dec += binint % 10 * (2 ** i)
        binint = binint // 10
        i += 1
    num = dec
    dec = int(num)
    octal = ""
    while dec > 0:
        octal = str(dec % 8) + octal
        dec = dec // 8
    return octal


# change number from binary to decimal
def bin_to_dec(num):
    binint = int(num)
    dec = 0
    i = 0
    while binint > 0:
        dec += binint % 10 * (2 ** i)
        binint = binint // 10
        i += 1
    return dec


# change number from decimal to binary
def dec_to_bin(num):
    dec = int(num)
    binnum = ''
    while dec > 0:
        binnum = str(dec % 2) + binnum
        dec = dec // 2
    return binnum


# change from decimal to hexadecimal
def dec_to_hexa(num):
    digits = "0123456789ABCDEF"
    x = (num % 16)
    rest = num // 16
    if (rest == 0):
        return digits[x]
    else:
        return dec_to_hexa(rest) + digits[x]


# change number decimal to octal
def dec_to_octal(num):
    dec = int(num)
    octal = ""
    while dec > 0:
        octal = str(dec % 8) + octal
        dec = dec // 8
    return octal


# change number from octal to binary
def octal_to_bin(num):
    octal = int(num)
    dec = 0
    i = 0
    while octal > 0:
        dec += octal % 10 * (8 ** i)
        octal = octal // 10
        i += 1
    num = dec
    dec = int(num)
    binnum = ''
    while dec > 0:
        binnum = str(dec % 2) + binnum
        dec //= 2
    return binnum


# change number from octal to decimal
def octal_to_dec(num):
    octal = int(num)
    dec = 0
    i = 0
    while octal > 0:
        dec += octal % 10 * (8 ** i)
        octal = octal // 10
        i += 1
    return dec


# change number octal to hexadecimal
def octal_to_hexa(num):
    octal = int(num)
    dec = 0
    i = 0
    while octal > 0:
        dec += octal % 10 * (8 ** i)
        octal = octal // 10
        i += 1
    num = dec
    digits = "0123456789ABCDEF"
    x = (num % 16)
    rest = num // 16
    if (rest == 0):
        return digits[x]
    else:
        return dec_to_hexa(rest) + digits[x]


# change number from hexadecimal to binary
def hexa_to_bin(num):
    k = counts = j = 0
    length = len(num) - 1
    length = int(length)
    while length >= 0:
        if num[length] >= '0' and num[length] <= '9':
            rem_1 = int(num[length])
        elif num[length] >= 'A' and num[length] <= 'F':
            rem_1 = ord(num[length]) - 55
        elif num[length] >= 'a' and num[length] <= 'f':
            rem_1 = ord(num[length]) - 87
        else:
            k = 1
            break
        counts = counts + (rem_1 * (16 ** j))
        length = length - 1
        j = j + 1

    if k == 0:
        print()
    else:
        print("\nInvalid Input!")
    dec = int(counts)
    binnum = ''
    while dec > 0:
        binnum = str(dec % 2) + binnum
        dec = dec // 2
    return binnum


# change number hexadecimal to octal
def hexa_to_octal(num):
    k = counts = j = 0
    length = len(num) - 1
    length = int(length)
    while length >= 0:
        if num[length] >= '0' and num[length] <= '9':
            rem_1 = int(num[length])
        elif num[length] >= 'A' and num[length] <= 'F':
            rem_1 = ord(num[length]) - 55
        elif num[length] >= 'a' and num[length] <= 'f':
            rem_1 = ord(num[length]) - 87
        else:
            k = 1
            break
        counts = counts + (rem_1 * (16 ** j))
        length = length - 1
        j = j + 1

    if k == 0:
        print()
    else:
        print("\nInvalid Input!")
    dec = int(counts)
    octal = ""
    while dec > 0:
        octal = str(dec % 8) + octal
        dec = dec // 8
    return octal


# change number from hexadecimal to decimal
def hexa_to_dec(num):
    k = counts = j = 0
    length = len(num) - 1
    length = int(length)
    while length >= 0:
        if num[length] >= '0' and num[length] <= '9':
            rem_1 = int(num[length])
        elif num[length] >= 'A' and num[length] <= 'F':
            rem_1 = ord(num[length]) - 55
        elif num[length] >= 'a' and num[length] <= 'f':
            rem_1 = ord(num[length]) - 87
        else:
            k = 1
            break
        counts = counts + (rem_1 * (16 ** j))
        length = length - 1
        j = j + 1

    if k == 0:
        return counts
    else:
        print("\nInvalid Input!")


while True:
    # menu1
    print('numbering system converter')
    print('A)insert a new number\nB) exit program')
    fst_input = str(input())
    if fst_input == "A":
        num = input("Please insert a number: ")
        # menu2
        print('please selact the base you want to convert a number from')
        print('A) decimal\nB) binary\nC) octal\nD) hexadecimal')
        snd_input = str(input())
        if snd_input == 'A':
            print('please select the base you want to covert a number to')
            print('A) decimal\nB) binary\nC) octal\nD) hexadecimal')
            thrd_input = str(input())
            if thrd_input == 'A':
                print(dec_to_dec(num))
            elif thrd_input == "B":
                print(dec_to_bin(num))
            elif thrd_input == "C":
                print(dec_to_octal(num))
            elif thrd_input == "D":
                print(dec_to_hexa(num))
            else:
                print('please select a valid choise')
        elif snd_input == 'B':
            print('please select the base you want to covert a number to')
            print('A) decimal\nB) binary\nC) octal\nD) hexadecimal')
            thrd_input = str(input())
            if thrd_input == 'A':
                print(bin_to_dec(num))
            elif thrd_input == "B":
                print(bin_to_bin(num))
            elif thrd_input == "C":
                print(bin_to_octal(num))
            elif thrd_input == "D":
                print(bin_to_hexa(num))
            else:
                print('please select a valid choise')
        elif snd_input == "C":
            print('please select the base you want to covert a number to')
            print('A) decimal\nB) binary\nC) octal\nD) hexadecimal')
            thrd_input = str(input())
            if thrd_input == 'A':
                print(octal_to_dec(num))
            elif thrd_input == "B":
                print(octal_to_bin(num))
            elif thrd_input == "C":
                print(octal_to_octal(num))
            elif thrd_input == "D":
                print(octal_to_hexa(num))
            else:
                print('please select a valid choise')
        elif snd_input == "D":
            print('please select the base you want to covert a number to')
            print('A) decimal\nB) binary\nC) octal\nD) hexadecimal')
            thrd_input = str(input())
            if thrd_input == 'A':
                print(hexa_to_dec(num))
            elif thrd_input == "B":
                print(hexa_to_bin(num))
            elif thrd_input == "C":
                print(hexa_to_octal(num))
            elif thrd_input == "D":
                print(hexa_to_hexa(num))
            else:
                print('please select a valid choise')
        else:
            print('please select a valid choise')

    elif fst_input == "B":
        exit()
    else:
        print('please select a valid choise')