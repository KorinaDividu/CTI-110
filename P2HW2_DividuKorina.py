#Korina Dividu
#06/21/2026
#P2HW2_DividuKorina.py
#The program stores the grades entered in a list

"""
Pseudocode:
#1. Collect grades for 6 modules from the user
#2. Store the grades in a list
#3. Display the lowest grade 
#4. Display the highest grade 
#5. Display the sum of grades
#6. Display the average by dividing the sum of grades by the number of modules
#7. Print the results 
"""

#Collecting grades
print("This program calculates the user's average for 6 modules.")

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

#Storing grades in a list
grades = [module1, module2, module3, module4, module5, module6]

#Calculations
Lowest_grade = min(grades)
Highest_grade = max(grades)
Sum_of_grades = sum(grades)
Average = Sum_of_grades / len(grades)

print("\n----------Results----------")
print(f"{'Lowest Grade: ':<18} {Lowest_grade}")
print(f"{'Highest Grade: ':<18} {Highest_grade}")
print(f"{'Sum of Grades: ':<18} {Sum_of_grades}")
print(f"{'Average: ':<18} {Average:.2f}")

print("_" * 27)
