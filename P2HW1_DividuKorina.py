#Korina Dividu
#06/21/2026
#P2HW1_DividuKorina.py
#This program calulates and displays travel expenses

#User input
print("This program calculates and displays travel expenses")

budget = float(input("\nEnter budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
hotel = float(input("\nApproximately, how much do you think you will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you think you need for food? "))

#calculations
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

#Output
print("\n----------Travel Expenses----------")
print(f"{'Location: ':<18} {destination}")
print(f"{'Initial Budget: ':<18} ${budget:>.2f}")
print(f"{'Fuel: ':<18} ${gas:>.2f}")
print(f"{'Accommodation: ':<18} ${hotel:>.2f}")
print(f"{'Food: ':<18} ${food:>.2f}")
print("_" * 35)

print(f"{'\nRemaining Balance: ':<18} ${remaining_balance:>.2f}")
