from collections import defaultdict
import networkx as nx
rows = open("Day20/data.txt").read().splitlines()

n_rows = len(rows)
n_columns = len(rows[0])

G = nx.Graph()
dirs = [(-1,0,True),(1,0,False),(0,-1,True),(0,1,False)]
labels = defaultdict(list)
for row_number, row in enumerate(rows):
  for column_number, cell in enumerate(row):
    if cell == ".":
      for off_x, off_y, reverse_label in dirs:
        x = column_number + off_x
        y = row_number + off_y
        if (0 <= x < len(row)) and (0 <= y < len(rows)):
          other = rows[y][x]
          if other == ".":
            G.add_edge((column_number,row_number,0), (x,y,0))
          if other.isupper():
            other2 = rows[y+ off_y][x+ off_x]
            if reverse_label:
              label = other2 + other
            else:
              label = other + other2
            labels[label].append((column_number,row_number))

# In the worst case,  each portal can lead to a new level.
number_of_levels = len([label for label,locs in labels.items() if len(locs) == 2])
levels = [G]
for level_number in range(1,number_of_levels+1):
  mapping = {n: (n[0],n[1],level_number) for n in G.nodes()}
  H = nx.relabel_nodes(G, mapping)
  levels.append(H)
G = nx.compose_all(levels)

def is_inner(locs):
  x,y = locs
  return x == 2 or y == 2 or y == (n_rows-3) or x == (n_columns - 3)

for label,locs in labels.items():
  if len(locs) == 2:
    lower, higher = locs
    if is_inner(higher):
      higher, lower = lower, higher
    for level_number in range(0,number_of_levels):
      G.add_edge((higher[0],higher[1],level_number), (lower[0],lower[1],level_number+1))

start = labels["AA"][0]
start = (start[0],start[1],0)
end = labels["ZZ"][0]
end = (end[0],end[1],0)

print(nx.shortest_path_length(G, source=start, target=end)) #7366