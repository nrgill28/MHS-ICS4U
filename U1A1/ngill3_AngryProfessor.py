"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_AngryProfessor.py
Description:
    Determines if a class is cancelled given some information
History . .:
    2/18/2020 - Created File
"""

# Read the number of test cases and run the loop that many times
test_cases = int(input())
for i in range(test_cases):
    # Get the first line of input and extract the threshold
    # (Ignore the number of students, we don't need it)
    inp = input().split()
    threshold = int(inp[1])

    # Get a list of all the arrival times
    arrival_times = [int(x) for x in input().split()]

    # Create a list of all the arrival times for students who were on-time
    on_time = [x for x in arrival_times if x <= 0]

    # If too many students are missing, cancel the class (print YES) otherwise print NO
    if len(on_time) < threshold: print("YES")
    else: print("NO")

