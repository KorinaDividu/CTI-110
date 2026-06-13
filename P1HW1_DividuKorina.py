#Korina Dividu
#06/14/2026
#p1hw1.py
#Calculating exponents and addition/subraction

#calculate exponents

print("--------Exponents--------")
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base ** exponent
print(base, "raised to the power of", exponent, "is", result, "!!")

# calculate addition and subtraction


print("--------Addition and Subtraction--------")
print()

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print(num1, "+", num2, "-", num3, "is equal to", final_result, "!!")


