# GradeBook Analyzer – Python CLI Project

A Python CLI tool that automates student mark analysis. It reads marks (manual or CSV), calculates statistics, assigns grades, shows pass/fail lists, and prints a formatted results table.

## Project Overview

The GradeBook Analyzer can:
- Accept manual input OR import a CSV file
- Calculate average, median, highest, and lowest marks
- Assign letter grades (A–F)
- Count grade distribution
- Generate pass/fail lists using list comprehension
- Display a formatted table
- Run repeatedly using a CLI loop

## Features

Input Methods:
- Manual entry of student names and marks
- CSV import (students.csv)

Statistics Provided:
- Average (mean)
- Median
- Maximum score
- Minimum score

Grade Rules:
A = 90+
B = 80–89
C = 70–79
D = 60–69
F = below 60

Pass/Fail Criteria:
- Pass: score ≥ 40
- Fail: score < 40

Sample Table Output :
Name        Marks      Grade
-----------------------------------
Alice       78         C
Bob         92         A
Charlie     55         D

CLI Menu:
1. Manual input
2. Load CSV
3. Exit program

## Project Structure

gradebook_analyzer/
- gradebook.py
- final_results.csv
- README.md

## How to Run

1. Run the script:
   python gradebook.py

2. Choose from the menu:
   1 = manual input
   2 = CSV import
   3 = exit

## CSV Format Example

name,marks,grade 
Alice,78,C  
Bob,92,A
Charlie,55,F  
Dave,39,F  
Emma,88,B  

## Requirements

If using only built-in modules:
csv


## Testing Checklist

- Minimum 5 manual entries tested
- At least one CSV tested
- All statistical functions work
- Grade distribution prints correctly
- Pass/fail lists work
- Table is formatted cleanly
- CLI loop works

## Author
Hiya 
