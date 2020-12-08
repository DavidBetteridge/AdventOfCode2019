lower = 178416
upper = 676461

def is_valid(number):
    if not (lower <= number <= upper):
        return False

    as_text = str(number)
    for i in range(0, len(as_text) - 1):
        if as_text[i] == as_text[i+ 1] : return True

    return False

good_passwords = 0
for n1 in range(1, 7):
    for n2 in range(n1, 10):
        for n3 in range(n2, 10):
            for n4 in range(n3, 10):
                for n5 in range(n4, 10):
                    for n6 in range(n5, 10):
                        toTry = int(f'{n1}{n2}{n3}{n4}{n5}{n6}')
                        if is_valid(toTry):
                            good_passwords += 1
print(good_passwords)                            
