from typing import List


Pack = List[int]

def factory_order(n: int) -> Pack:
  return list(range(0, n))

def deal_into_new_stack(pack: Pack) -> Pack:
  return pack[::-1]

def cut(pack: Pack, n: int) -> Pack:
  return pack[n:] + pack[:n]

def deal_with_increment_N(pack: Pack, n: int) -> Pack:
  new_pack = [0] * len(pack)
  j = 0
  i = 0
  while i < len(pack):
    new_pack[j] = pack[i]
    i += 1
    j = (j + n) % len(pack)
  return new_pack

pack = [0,1,2,3,4,5,6,7,8,9]
assert deal_into_new_stack(pack) == [9,8,7,6,5,4,3,2,1,0]

pack = [0,1,2,3,4,5,6,7,8,9]
assert cut(pack, 3) == [3,4,5,6,7,8,9,0,1,2]

pack = [0,1,2,3,4,5,6,7,8,9]
assert cut(pack, -4) == [6,7,8,9,0,1,2,3,4,5]

pack = [0,1,2,3,4,5,6,7,8,9]
assert deal_with_increment_N(pack, 3) == [0,7,4,1,8,5,2,9,6,3]


def shuffle(number_of_cards: int, filename: str) -> Pack:
  pack = factory_order(number_of_cards)
  with open(filename) as f:
    for command in f:
      match command.strip().split():
        case ["deal","with","increment",n]:
          pack = deal_with_increment_N(pack, int(n))
        case ["deal","into","new","stack"]:
          pack = deal_into_new_stack(pack)
        case ["cut",n]:
          pack = cut(pack, int(n))
  return pack


assert shuffle(10, "Day22/sample1.txt") == [0,3,6,9,2,5,8,1,4,7]
assert shuffle(10, "Day22/sample2.txt") == [3,0,7,4,1,8,5,2,9,6]
assert shuffle(10, "Day22/sample3.txt") == [6,3,0,7,4,1,8,5,2,9]
assert shuffle(10, "Day22/sample4.txt") == [9,2,5,8,1,4,7,0,3,6]

shuffled = shuffle(10007 , "Day22/data.txt")
print(shuffled.index(2019))
assert shuffled.index(2019) == 7545
