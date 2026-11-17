# Take how many hours, wage, basic salary as input for 5 worker
# U must write this formula for each one to calculate final
# (hours - 20) * wage - basic
# Then you must insert final salary in a list for each one
# and provide the highest.
# Initialize an empty list to store the final salaries



# Initialize an empty list to store the final salaries
final_salaries = []

# Loop to get input for 5 workers
for i in range(1, 6):
    print(f"--- Worker {i} ---")
    
    # Taking inputs
    hours = float(input(f"Enter hours worked for worker {i}: "))
    wage = float(input(f"Enter hourly wage for worker {i}: "))
    basic = float(input(f"Enter basic salary for worker {i}: "))
    
    # Calculating final salary using the formula: (hours - 20) * wage - basic
    final_salary = (hours - 20) * wage - basic
    
    # Appending the result to the list
    final_salaries.append(final_salary)
    print(f"Calculated Final Salary: {final_salary:.2f}\n")

print("--- Results ---")
print(f"All final salaries: {final_salaries}")

# --- Finding the highest salary WITHOUT using max() ---
# Step 1: Assume the first worker's salary is the highest to start with
highest_salary = 0

# Step 2: Loop through the list and compare each salary
for salary in final_salaries:
    if salary > highest_salary:
        highest_salary = salary  # Update highest_salary if a larger one is found

print(f"The highest final salary is: {highest_salary:.2f}")
