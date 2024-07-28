
# Week1 Assignment
**Programming Language Used**: Python 
## Step by step Solution:

1.	**Get User Input:** Prompt the user for values of n and k.
2.	**Initialize Variables:** Set up variables to keep track of the smallest relative miss and the corresponding values of x, y, and z.
3.	**Loop through x and y values:** Use nested loops to iterate over possible values of x and y within the specified range.
4.	**Calculate x^n + y^n:** For each combination of x and y, calculate x^n + y^n.
5.	**Find z that Brackets the Result:** Find the integer z such that z^n <= x^n + y^n < (z+1)^n.
6.	**Calculate the Miss:** Determine the miss and the relative miss for both z and z+1.
7.	**Update the Smallest Miss:** Keep track of the smallest relative miss found so far and print out the results.
8.	**Output Results:** After completing the loops, print the smallest relative miss and the corresponding x, y, and z.

## Python code:
``` python
import math

def find_near_misses(n, k):
    smallest_miss = float('inf')
    best_x, best_y, best_z = 0, 0, 0

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            lhs = x**n + y**n
            z = int(lhs**(1/n))
            z1 = z + 1

            miss1 = abs(lhs - z**n)
            miss2 = abs(lhs - z1**n)
            miss = min(miss1, miss2)
            relative_miss = miss / lhs

            if relative_miss < smallest_miss:
                smallest_miss = relative_miss
                best_x, best_y, best_z = x, y, z if miss1 < miss2 else z1
                best_actual_miss = miss

            print(f"x: {x}, y: {y}, z: {best_z}, miss: {miss}, relative miss: {relative_miss:.6f}")

    print("####################")
    print(f"Actual miss: {best_actual_miss} Smallest relative miss: {smallest_miss:.6f} for x: {best_x}, y: {best_y}, z: {best_z}")

if __name__ == "__main__":
    while True:
        # Input from user
        n = int(input("Enter the power n (2 < n < 12): "))
        k = int(input("Enter the limit k (k > 10): "))
        
        # Validate input range for n
        if n <= 2 or n >= 12:
            print("Error: n must be greater than 2 and less than 12.")
        elif k <= 10:
            print("Error: k must be greater than 10.")
        else:
            find_near_misses(n, k)
        
        # Ask user if they want to continue or exit
        choice = int(input("Press 1 to continue or 0 to exit: "))
        if choice == 0:
            break
```
### Code Explanation:

The function find_near_misses(n, k) takes two parameters:

(n): The power (should be between 3 and 11).

(k): The limit (should be greater than 10).

It iterates through combinations of (x) and (y) within the specified range (from 10 to (k)).

For each combination, it calculates the left side of the expression: (x^n + y^n).

Then, it computes (z) as the integer part of the (n)th root of the left side.

The function also calculates two types of misses:

(miss1): The absolute difference between the left side and (z^n).

(miss2): The absolute difference between ((z + 1)^n) and the left side.

The actual miss is the smaller of (miss1) and (miss2).

The relative miss is the actual miss divided by the left side.

Steps in the Code:

Initialize variables to track the best values found: smallest_relative_miss, best_x, best_y, best_z, and best_actual_miss.

Nested loops iterate over values of (x) and (y).

For each combination:

Calculate the left side: (x^n + y^n).

Compute (z) using the (n)th root of the left side.

Calculate the actual miss and relative miss.

Update the best values if the relative miss is 
smaller than the current smallest relative miss.

Print the best combination of (x), (y), and (z) along with their actual miss and relative miss.

while loop helps in continuous execution of code if you want to continue press1 or if you want to exit press 0


## Code execution:

I ran the above mentioned code by giving n and k values as 5 and 12 and the output I got is given below:

```
Enter the power n (2 < n < 12): 5
Enter the limit k (k > 10): 12
x: 10, y: 10, z: 11, miss: 38949, relative miss: 0.194745
x: 10, y: 11, z: 12, miss: 12219, relative miss: 0.046807
x: 10, y: 12, z: 12, miss: 22461, relative miss: 0.064389
x: 11, y: 10, z: 12, miss: 12219, relative miss: 0.046807
x: 11, y: 11, z: 12, miss: 49191, relative miss: 0.152719
x: 11, y: 12, z: 12, miss: 38590, relative miss: 0.094149
x: 12, y: 10, z: 12, miss: 22461, relative miss: 0.064389
x: 12, y: 11, z: 12, miss: 38590, relative miss: 0.094149
x: 12, y: 12, z: 12, miss: 40160, relative miss: 0.080697
####################
Actual miss: 12219 Smallest relative miss: 0.046807 for x: 10, y: 11, z: 12
```
## Steps and instructions to run the code:
There are two possible ways to run the code. 
### 1St option:
Just click on  the Fermants-Near_Miss_Finder.exe file and  gave values of n, k. After execution of code it will ask two options whether you want to continue the execution of code or exit from the code. press 1 if you want to continue , else press 0 it will break exexcution

### 2nd option:
First download the python file named "Fermants_Near_Miss_Finder.py" into your local machine, then use any of python IDE's Such as pycharm or jupyter notebooks or google colab  to run the code. After running code the program asks you to enter the value of n, there enter n value  greater than 2 and less than 12. After entering n value the program asks you to enter k value, here you enter k value greater than 10, then it will execute the algorithms and give output on numbers having smallest relative miss. if you not enter n and k values as 2< n >12 and  k>10 respectively . the program ends with showing errors. After execution of code it will ask two options whether you want to continue the execution of code or exit from the code. press 1 if you want to continue , else press 0 it will break exexcution







