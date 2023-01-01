from Computer import Computer

# Load the program
text = open(r"C:\Personal\AdventOfCode2019\Day19\data.txt").read()
s = text.split(',')
memory = {}
for i in range(len(s)):
    memory[i] = int(s[i])

def query(row, column):
  input_no = 0
  def read_from_keyboard():
    nonlocal input_no
    if input_no == 0:
      input_no+=1
      return row
    else:
      return column

  answer = None
  def output_to_screen(valueToPrint):
    nonlocal answer
    answer = valueToPrint

  com = Computer(memory.copy())
  com.run_program(read_from_keyboard, output_to_screen)
  return answer

# Find the first row of width 100
row = 1
start = 0
end = 0
width = 1
while width < 100:
  # Start
  if query(row,start) == 0:
    start = start + 1
  if query(row, end+1) == 1:
    end = end + 1
  width = end-start+1
  row+=1
print(row, start, end, width)

rows = {}
rows[row] = (start,end)
window_start = row
window_end = row

while window_end - window_start + 1 < 100:
  # Find the width of the following row
  window_end+=1
  if query(window_end,start) == 0:
    start = start + 1
  if query(window_end, end+1) == 1:
    end = end + 1
  rows[window_end] = (start,end)

  # Do we need to move the start of the window forward?
  while (window_start < window_end) and (rows[window_start][1] - rows[window_end][0] + 1) < 100:
    window_start += 1

print(window_start, rows[window_start][0], rows[window_start][1])
print(window_end, rows[window_end][0], rows[window_end][1])

print( (rows[window_end][0] * 10000) + window_start)  # 7131432 too low


