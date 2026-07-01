#Korina Dividu
#06/28/2026
#P3HW1_DividuKorina.py
#Debugging a program

#Enter grades for six modules
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

#Add grades entered to a list
grades = [module1, module2, module3, module4, module5, module6]

#Determine lowest, highest, sum, and average for grades
Lowest_grade = min(grades)
Highest_grade = max(grades)
Sum_of_grades = sum(grades)
Average = Sum_of_grades / len(grades)

#Determine letter grade for average
if Average >= 90:
        letter_grade = "A"
elif Average >= 80:
        letter_grade = "B"
elif Average >= 70:
        letter_grade = "C"
elif Average >= 60:
        letter_grade = "D"
else:
        letter_grade = "F" 


#Display results
print("\n----------Results----------")
print(f"{'Lowest Grade: ':<18} {Lowest_grade}")
print(f"{'Highest Grade: ':<18} {Highest_grade}")
print(f"{'Sum of Grades: ':<18} {Sum_of_grades}")
print(f"{'Average: ':<18} {Average:.2f}")

print("_" * 27)

print(f"Your grade is: {letter_grade}")