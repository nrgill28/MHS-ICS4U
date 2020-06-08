k = 10
for y in range(9):
    for x in range(y + 1):
        print(k, end=' ')
        k += 1
    print()

box_size = int(input("\nBox size: "))
print('o' * box_size)
if box_size > 2:
    for _ in range(box_size - 2):
        print('o' + (' ' * (box_size - 2)) + 'o')
if box_size > 1:
    print('o' * box_size)

print()

for y in range(box_size * 2):
    for x in range(box_size * 2):
        if x <= box_size and y <= box_size:
            print(
                1 + (2 * (x + y))
                if x + y <= box_size - 1
                else " ", end=' '
            )
        elif x > box_size >= y:
            print(
                1 + (2 * ((2 * box_size - (x + 1)) + y))
                if (2 * box_size - (x + 1)) + y <= box_size - 1
                else " ", end=' '
            )
        elif x <= box_size < y:
            print(
                1 + (2 * (x + (2 * box_size - (y + 1))))
                if x + (2 * box_size - (y + 1)) <= box_size - 1
                else " ", end=' '
            )
        else:
            print(
                1 + (2 * ((2 * box_size - (x + 1)) + (2 * box_size - (y + 1))))
                if (2 * box_size - (x + 1)) + (2 * box_size - (y + 1)) <= box_size - 1
                else " ", end=' '
            )
    print()

"""
for y in range(box_size * 2):
    for x in range(box_size * 2):
        print(1 + (2 * ((2 * box_size - x) + y)) if (2 * box_size - x) + y <= box_size - 1 else " ", end=' ')
    print()
"""
