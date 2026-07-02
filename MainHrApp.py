def calculate_bonus(base_salary, performance_rating):
    base_salary = float(base_salary)
    performance_rating = int(performance_rating)
    if performance_rating == 5:
        bonus = base_salary * 0.2
    elif performance_rating == 4 or performance_rating == 3:
        bonus = base_salary * 0.1
    else:
        bonus = 0
    return bonus

def tax(base_salary,bonus):
    grossSalary = float(base_salary + bonus)
    if grossSalary > 7000:
        tax_amount = grossSalary * 0.15
    elif 3000 < grossSalary <= 7000:
        tax_amount = grossSalary * 0.1
    else:
        tax_amount = 0
    return tax_amount

def mainHrApp():
    name = input("Please enter your name: ").strip()
    base_salary = float(input("Please enter your base salary: ").strip())
    performance_rating = int(input("Please enter your performance rating (1-5): ").strip())
    
    if performance_rating < 1 or performance_rating > 5 or base_salary < 0:
        print("Invalid data entered. Please restart and check your inputs.")
        return
    
    department = input("Please enter your department: ").strip()
    bonus = calculate_bonus(base_salary, performance_rating)
    tax_amount = tax(base_salary, bonus)
    net_salary = base_salary + bonus - tax_amount

    print(f"Hello {name}, \nyour base salary is: ${base_salary}, \nyour bonus is: ${bonus}", 
           f"\nAnd your tax amount is: ${tax_amount}, \nYour net salary " 
             f"after tax is: ${net_salary}.")    

mainHrApp()
