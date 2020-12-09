LOWER = 178416
UPPER = 676461

def is_valid_for_part_one(password):
    return any(password[i] == password[i + 1] for i in range(0, 5))

def is_valid_for_part_two(password):
    return any(password[i] == password[i + 1] and password.count(password[i]) == 2 for i in range(0, 5))

def possible_passwords():
    for n1 in range(1, 7):
        for n2 in range(n1, 10):
            for n3 in range(n2, 10):
                for n4 in range(n3, 10):
                    for n5 in range(n4, 10):
                        for n6 in range(n5, 10):
                            number = f'{n1}{n2}{n3}{n4}{n5}{n6}'
                            if (LOWER <= int(number) <= UPPER):
                                yield number

def part_one():
    return sum([is_valid_for_part_one(x) for x in possible_passwords()])

def part_two():
    return sum([is_valid_for_part_two(x) for x in possible_passwords()])

def part_two_two():
    return sum([any(password[i] == password[i + 1] and password.count(password[i]) == 2 for i in range(0, 5)) for password in possible_passwords()])    

