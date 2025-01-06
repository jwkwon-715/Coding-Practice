n = int(input())
count = 0

for i in range(n+1):
  for j in range(60):
    for l in range(60):
      if '3' in str(i)+str(j)+str(l):
        count += 1

print(count)
