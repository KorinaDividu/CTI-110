#Korina Dividu
#06/14/2026
#p1hw2_DividuKorina.py
#Calulate and display travel budget

"""
Pseudocode:
1. Ask user to enter their budget
2. Ask user to enter travel destination
3. Ask user for amount they will spend on gas
4. Ask user for amount they will spend on accommodations
5. Ask user for amount they will spend on food
6. Add expenses
7. Subtract expenses from budget
8. Display remaining balance
"""

print("This program calculates and displays travel expenses")


budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas: "))
hotel = int(input("Approximately, how much will you need for accommodation/hotels: "))
food = int(input("Last, how much do you need for food: "))

remaining = budget - gas - hotel - food 

print("--------Travel Expenses--------")


print("Location: ", destination)
print("Initial Budget: ", budget)
print("Fuel: ", gas)
print("Accommodation: ", hotel)
print("Food: ", food)

print("Remaining Budget: ", remaining)
