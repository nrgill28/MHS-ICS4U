"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_U5T2_1.py
Description:
    CSV Exercises
History . .:
    5/04/2020 - Created File
"""
import csv
import random


def exercise_1():
    with open(csv_file) as fp:
        csv_reader = csv.reader(fp)
        for line in csv_reader:
            print(", ".join(line))


def exercise_2():
    with open(csv_file) as fp:
        csv_reader = csv.reader(fp, delimiter='\t')
        for line in csv_reader:
            print(", ".join(line))


def exercise_3():
    with open(csv_file) as fp:
        csv_reader = csv.reader(fp)
        print(list(csv_reader))


def exercise_4():
    with open(csv_file) as fp:
        csv_reader = csv.DictReader(fp)
        for line in csv_reader:
            print(line)


def exercise_5():
    with open(csv_file) as fp:
        csv_reader = csv.reader(fp, skipinitialspace=True)
        for line in csv_reader:
            print(", ".join(line))


def exercise_6():
    with open(csv_file) as fp:
        csv.register_dialect('dialect', quoting=csv.QUOTE_ALL, delimiter='|', skipinitialspace=True)
        csv_reader = csv.reader(fp, dialect="dialect")
        for line in csv_reader:
            print(", ".join(line))


def exercise_7():
    with open(csv_file) as fp:
        csv_reader = csv.reader(fp)
        width = len(next(csv_reader))
        indices = random.choices(range(width), k=2)
        fp.seek(0)
        for line in csv_reader:
            print(", ".join([line[i] for i in indices]))


def exercise_8():
    with open(csv_file) as fp:
        csv_reader = csv.reader(fp)
        headers = next(csv_reader)
        for line in csv_reader:
            print(", ".join(line))
        print(f"\nTotal Lines: {csv_reader.line_num}\nHeaders:\n{', '.join(headers)}")


def exercise_9():
    with open(csv_file, 'w') as fp:
        csv_writer = csv.writer(fp, lineterminator='\n')
        csv_writer.writerow(["char", "decimal", "hexadecimal", "binary"])
        for i in range(ord('a'), ord('z')+1):
            csv_writer.writerow([chr(i), str(i), hex(i), bin(i)])
    print("(Wrote File)")


def exercise_10():
    data = [[chr(i), str(i), hex(i), bin(i)] for i in range(ord('A'), ord('Z')+1)]
    with open(csv_file, 'w') as fp:
        csv_writer = csv.writer(fp, lineterminator='\n')
        csv_writer.writerow(["char", "decimal", "hexadecimal", "binary"])
        csv_writer.writerows(data)

    with open(csv_file, 'r') as fp:
        csv_reader = csv.reader(fp)
        for line in csv_reader:
            print(", ".join(line))


def exercise_11():
    data = [{
        "char": chr(i),
        "decimal": str(i),
        "hexadecimal": hex(i),
        "binary": bin(i)
    } for i in range(32, 127)]
    headers = ["char", "decimal", "hexadecimal", "binary"]

    with open(csv_file, 'w') as fp:
        csv_writer = csv.DictWriter(fp, lineterminator='\n', fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(data)

    with open(csv_file, 'r') as fp:
        csv_reader = csv.reader(fp)
        for line in csv_reader:
            print(", ".join(line))


methods = [
    exercise_1, exercise_2, exercise_3,
    exercise_4, exercise_5, exercise_6,
    exercise_7, exercise_8, exercise_9,
    exercise_10, exercise_11
]
csv_file = input("Input/Output File: ")
if not csv_file:
    csv_file = "sample.csv"

while True:
    try:
        exercise = int(input(f"Which task? (1-{len(methods)}, anything else to exit): "))
        if not 1 <= exercise <= len(methods):
            break
    except ValueError:
        break
    methods[exercise-1]()
