fishes = [5, 1, 1, 3, 1, 1, 5, 1, 2, 1, 5, 2, 5, 1, 1, 1, 4, 1, 1, 5, 1, 1, 4, 1, 1, 1, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 5, 1, 1, 1, 4, 1, 1, 1, 1, 1, 3, 1, 1,
         4, 1, 4, 1, 1, 2, 3, 1, 1, 1, 1, 4, 1, 2, 2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 4, 2, 1, 1, 1, 1, 1, 4, 3, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 2, 1,
         1, 1, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 3, 1, 2, 1, 1, 4, 1, 1, 5, 3, 1, 1, 1, 2, 4, 1, 1, 2, 4, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1,
         1, 1, 4, 3, 1, 2, 1, 2, 1, 5, 1, 2, 1, 1, 5, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 3, 1, 1, 5, 1, 1, 1, 1,
         5, 1, 4, 1, 1, 1, 4, 1, 3, 4, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 5, 1, 3, 1, 1, 1, 1, 4, 1, 5, 3, 1, 1, 1, 1, 1, 5, 1, 1, 1, 2, 2]

for day in range(80):
    print(day)
    for idx in range(len(fishes)):
        fishes[idx] -= 1
        if fishes[idx] < 0:
            fishes[idx] = 6
            fishes.append(8)

print(f'Amount of fish after 80 days: {len(fishes)}')
