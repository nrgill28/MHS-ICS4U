# U1A1 - Python Review

### 1. Simple Decision Making
Write a program that asks the user to enter a number of seconds and works as follows:
There are 60 seconds in a minute. If the number of seconds entered by the user is greater
than or equal to 60, the program should display the number of minutes in that many
Seconds.
There are 3,600 seconds in an hour. If the number of seconds entered by the user is
greater than or equal to 3,600, the program should display the number of hours in that
many seconds.
There are 86,400 seconds in a day. If the number of seconds entered by the user is
greater than or equal to 86,400, the program should display the number of days in that
many seconds.  
Save your program as YourName_TimeCalculator.py

### 2. Simple Loop
Write a program that predicts the approximate size of a population of organisms. The application should use inputs to allow the user to enter the starting number of organisms, the average daily population increase (as a percentage), and the number of days the organisms will be left to multiply. For example, assume the user enters the following values:
Starting number of organisms: 2
Average daily increase: 30%
Number of days to multiply: 10
The program should display the following table of data:

| Day | Approximate Population |
| --- | ---------------------- |
| 1   | 2                      |
| 2   | 2.6                    |
| 3   | 3.38                   |
| 4   | 4.394                  |
| 5   | 5.7122                 |
| 6   | 7.42586                |
| 7   | 9.653619               |
| 8   | 12.5497                |
| 9   | 16.31462               |
| 10  | 21.209                 |

Save your program as YourName_Population.py

## 3. Simple Nested Loop
Write a program that uses nested loops to draw this pattern:
```##
# #
#  #
#   #
#    #
#     #
```
Save your program as YourName_NestedSymbols.py

### 4. Simple Functions
Write a function called chorus that accepts no arguments and prints the words to the chorus of “Eye of the Tiger”, by Survivor. Write a program that displays all of the lyrics to the song and calls on the function at the appropriate time.  
Save your program as YourName_Lyrics.py

### 5. Simple Functions with Arguments
Write a function named max that accepts two integer values as arguments and returns the
value that is the greater of the two. For example, if 7 and 12 are passed as arguments to
the function, the function should return 12. Use the function in a program that prompts the
user to enter two integer values. The program should display the value that is the greater
of the two.  
Save your program as YourName_TheGreatest.py

### 6. Simple Functions with Arguments and Returned Value
Suppose you have a certain amount of money in a savings account that earns compound
monthly interest, and you want to calculate the amount that you will have after a specific
number of months. The formula is as follows:
`F=P+it`
The terms in the formula are:
- F is the future value of the account after the specified time period.
- P is the present value of the account.
- i is the monthly interest rate.
- t is the number of months.

Write a program that prompts the user to enter the account’s present value, monthly interest
rate, and the number of months that the money will be left in the account. The program
should pass these values to a function that returns the future value of the account, after the
specified number of months. The program should display the account’s future value.  
Save your program as YourName_MoMoneyMoProblems.py


### 7. Bringing It All Together (Part 1)
Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.  
Save your program as YourNameRockPaperScissors.py

### 8. Bringing It All Together (Part 2)
A Discrete Mathematics professor has a class of  students. Frustrated with their lack of discipline, he decides to cancel class if fewer than `N` students are present when class starts.

Given the arrival time of each student, determine if the class is canceled.

**Input Format:**  
The first line of input contains `T`, the number of test cases.

Each test case consists of two lines. The first line has two space-separated integers, `N` (students in the class) and `K` (the cancellation threshold). The second line contains space-separated integers (`a1,a2,a3,...an,`) describing the arrival times for each student.

Note: Non-positive arrival times (`ai0`) indicate the student arrived early or on time; positive arrival times (`ai>0`) indicate the student arrived `ai` minutes late.

**Constraints:**
- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 1000
- 1 ≤ K ≤ N
- -100 ≤ ai ≤ 100, where i∈[1,N]

**Output Format:**

For each test case, print the word YES if the class is canceled or NO if it is not.

**Note:**   
If a student arrives exactly on time (ai=0) , the student is considered to have entered before the class started.

**Sample Input:**
```
2
4 3
-1 -3 4 2
4 2
0 -1 2 1
```
**Sample Output:**
```
YES
NO
```
Save your program as YourName_AngryProfessor.py
