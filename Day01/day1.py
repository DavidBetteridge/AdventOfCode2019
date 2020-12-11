import math

masses = list(map(int, open('Day01/day1.txt').read().splitlines()))

def calculate_fuel(mass):
    return math.floor(mass / 3) - 2

def calculate_fuel_plus_fuel(mass):
    fuelRequired = math.floor(mass / 3) - 2
    if fuelRequired < 0: return 0

    return fuelRequired + calculate_fuel_plus_fuel(fuelRequired)

def part_one():
    return sum([calculate_fuel(mass) for mass in masses])

def part_two():
    return sum([calculate_fuel_plus_fuel(mass) for mass in masses])       