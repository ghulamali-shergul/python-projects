# Tip Calculator
print("Welcome to the tip calculator!")

# Ask the user for the total bill, the tip percentage, and the number of people to split the bill
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? ")) 

# Calculate the tip amount, the total bill with tip, and the amount each person should pay
tip_as_percent = tip_percentage / 100
total_tip_amount = total_bill * tip_as_percent
total_bill_with_tip = total_bill + total_tip_amount
per_person = total_bill_with_tip / people
final_amount = round(per_person, 2)

# Display the amount each person should pay
print(f"Each person should pay: ${final_amount}")
