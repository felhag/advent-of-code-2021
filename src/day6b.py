fishes = [5, 1, 1, 3, 1, 1, 5, 1, 2, 1, 5, 2, 5, 1, 1, 1, 4, 1, 1, 5, 1, 1, 4, 1, 1, 1, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 5, 1, 1, 1, 4, 1, 1, 1, 1, 1, 3, 1, 1,
          4, 1, 4, 1, 1, 2, 3, 1, 1, 1, 1, 4, 1, 2, 2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 4, 2, 1, 1, 1, 1, 1, 4, 3, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 2, 1,
          1, 1, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 3, 1, 2, 1, 1, 4, 1, 1, 5, 3, 1, 1, 1, 2, 4, 1, 1, 2, 4, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1,
          1, 1, 4, 3, 1, 2, 1, 2, 1, 5, 1, 2, 1, 1, 5, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 3, 1, 1, 5, 1, 1, 1, 1,
          5, 1, 4, 1, 1, 1, 4, 1, 3, 4, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 5, 1, 3, 1, 1, 1, 1, 4, 1, 5, 3, 1, 1, 1, 1, 1, 5, 1, 1, 1, 2, 2]

days = dict.fromkeys(range(0, 9), 0)
for fish in fishes:
    days[fish] += 1

for day in range(256):
    print(day)

    born = days[0]
    for idx in range(1, 9):
        days[idx - 1] = days[idx]

    days[6] += born
    days[8] = born

print(f'Amount of fish after 256 days: {sum(days.values())}')
