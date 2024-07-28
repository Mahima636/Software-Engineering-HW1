"""
Title: Fermat's Near Miss Finder
File: Fermant's_Near_Miss_Finder.py
Created Files: None
Name : Mahima devaraj, Sandeep Reddy Bapathu
Email: MahimaDevaraja@lewisu.edu, SandeepReddyBapath@lewisu.edu
student ID's: L30081389(Mahima devraj),L30088103 (Sandeep Reddy Bapathu)
Course Name, Number & section : Software Engineering,  CPSC 60500, Section 1, Summer 2024
Date: 07/28/2024
Description: This program finds near misses for the equation x^n + y^n = z^n for n in the range 3-11 and x, y in the range 10-k.
Resources:https://www.youtube.com/watch?v=ReOQ300AcSU
"""
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
