import math

class Chemical:
    def __init__(self, name, quantity):
        self.Name = name
        self.Quantity = quantity

    def __repr__(self):
        return f'{self.Quantity} x {self.Name}'

class State:
    def __init__(self):
        self.Ore = 0
        self.Spare = {}

    def in_stock(self, chemical):        
        if chemical in self.Spare:
            return self.Spare[chemical]
        else:
            return 0 

    def add_to_store(self, chemical, extra):        
        if chemical in self.Spare:
            self.Spare[chemical] = self.Spare[chemical] + extra
        else:
            self.Spare[chemical] = extra

    def take_from_store(self, chemical, quantity_needed):        
        if not chemical in self.Spare:
            return quantity_needed
        elif self.Spare[chemical] > quantity_needed:
            self.Spare[chemical] = self.Spare[chemical] - quantity_needed
            return 0 
        else:
            left = quantity_needed - self.Spare[chemical]
            self.Spare[chemical] = 0
            return left


reactions = {}
for reaction in open('Day14/day14.txt').read().splitlines():
    inputs, output = reaction.split(' => ')
    makes_quantity, makes_chemical = output.split(' ')
    inputs = inputs.split(', ')
    makes = Chemical(makes_chemical, int(makes_quantity))

    ingredients = []
    for input in inputs:
        quantity, name = input.split(' ')
        ingredient = Chemical(name, int(quantity))
        ingredients.append(ingredient)

    reactions[makes.Name] = (ingredients, makes)        

def make(ingredientName, quantity_needed, state):

    #  We need 3 lots of A
    #  Rule  9 ORE => 2A

    # First check stock for any As
    remaining_needed = state.take_from_store(ingredientName, quantity_needed)
    if remaining_needed == 0: return

    # Work out how to make an 'A'
    ingredients, makes = reactions[ingredientName] 

    # How many lots do we need to make in order to at least reach the quantity needed
    lots_to_make = math.ceil(remaining_needed / makes.Quantity)

    # Now many extra does that make?
    made_extra = (lots_to_make * makes.Quantity) - remaining_needed

    # How do we make it?
    for ingredient in ingredients:    
        if ingredient.Name == "ORE":
            state.Ore += ingredient.Quantity * lots_to_make
        else:
            make(ingredient.Name, ingredient.Quantity * lots_to_make, state)

    # Put the extra into stock
    if made_extra > 0:
        state.add_to_store(ingredientName, made_extra)

def ore_needed_to_make_fuel(quantity):
    fuel = reactions['FUEL']
    state = State()
    for ingredient in fuel[0]:
        make(ingredient.Name, quantity * ingredient.Quantity, state)
    return state.Ore

def part_one():
    return ore_needed_to_make_fuel(1)

def part_two():
    target = 1000000000000      #1e9
    lowerBound = 1
    upperBound = 1000000000000

    while lowerBound < upperBound:
        quantity_to_try = math.floor((upperBound + lowerBound) / 2)
        ore = ore_needed_to_make_fuel(quantity_to_try)
        if ore == target:
            return quantity_to_try
        elif ore < target:
            lowerBound = quantity_to_try + 1
        else:
            upperBound = quantity_to_try - 1
    return lowerBound - 1

print(part_two())