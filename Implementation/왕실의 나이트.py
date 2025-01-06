input_data = input()
row = input_data[1]
column = ord(input_data[0].lower()) - ord('a') +1

steps = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]

count = 0

for step in steps:
  next_row = row + step[i]
  next_column = column + step[i]
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    count += 1

print(count)
