# HR Salary & Bonus Calculator

A simple, interactive command-line Python application designed for HR administrators to calculate employee bonuses, tax deductions, and final net salaries based on performance ratings and base salaries.

---

## Features

* **Dynamic Bonus Calculation:** Automatically calculates bonuses based on employee performance ratings (1 to 5).
* **Progressive Tax Deductions:** Applies a tiered tax rate based on the employee's gross salary (Base Salary + Bonus).
* **Input Validation:** Basic checks to ensure input values (like performance ratings and salaries) fall within valid ranges.

---

## How It Works

### 1. Bonus Breakdown
The application calculates bonuses as a percentage of the base salary using the following tiers:
* **Rating 5:** 20% Bonus
* **Rating 3 or 4:** 10% Bonus
* **Rating 1 or 2:** 0% Bonus

### 2. Tax Breakdown
Tax rates are applied to the **Gross Salary** (Base Salary + Bonus) based on the following brackets:
* **Gross Salary > $7,000:** 15% tax
* **Gross Salary between $3,001 and $7,000:** 10% tax
* **Gross Salary $3,000 or less:** 0% tax

---

## Prerequisites

To run this script, you only need to have **Python 3.x** installed on your system.

## Getting Started

1. **Clone or Download the Script:**
   Save the Python code into a file named `MainHrApp.py`.

2. **Run the Application:**
   Open your terminal or command prompt, navigate to the folder containing the file, and execute:
   ```bash
   python MainHrApp.py
## Example Usage

Please enter your name: Lian
Please enter your base salary: 6000
Please enter your performance rating (1-5): 5
Please enter your department: Engineering

Hello Lian, 
your base salary is: $6000.0, 
your bonus is: $1200.0 
And your tax amount is: $1080.0, 
Your net salary after tax is: $6120.0.
