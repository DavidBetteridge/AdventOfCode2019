from collections import defaultdict
import networkx as nx
rows = open("Day20/data.txt").read().splitlines()

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
            G.add_edge((column_number,row_number), (x,y))
          if other.isupper():
            other2 = rows[y+ off_y][x+ off_x]
            if reverse_label:
              label = other2 + other
            else:
              label = other + other2
            labels[label].append((column_number,row_number))

for label,locs in labels.items():
  if len(locs) == 2:
    G.add_edge(*locs)

start = labels["AA"][0]
end = labels["ZZ"][0]

print(nx.shortest_path_length(G, source=start, target=end))