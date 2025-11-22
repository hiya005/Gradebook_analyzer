# Name: Hiya
# Date: 23 Nov 2025
# Title: GradeBook Analyzer
# Description:
#  A Python CLI tool that reads student marks manually or  from a CSV file, performs statistical analysis, assigns grades,  prints a complete summary and Exports final results to CSV.

import csv
from datetime import datetime

# MENU DISPLAY #
def show_menu():
    print("\n GradeBook Analyzer ")
    print("1. Enter student data manually")
    print("2. Load data from CSV file")
    print("3. Exit")

print("Welcome to the GradeBook Analyzer!")

# MANUAL INPUT #
def manual_input():
    marks = {}
    n = int(input("How many students? "))

    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        score = float(input(f"Enter marks for {name}: "))
        marks[name] = score
    
    return marks

#  CSV INPUT  #
def load_from_csv():
    marks = {}
    file = input("Enter CSV file path ): ")

    try:
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                marks[row["Name"]] = float(row["Marks"])
    except FileNotFoundError:
        print("Error: File not found. Please try again.")
        return {}
    
    return marks

# STATISTICAL FUNCTIONS  #
def calculate_average(marks_dict):
    if len(marks_dict) == 0:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    scores = sorted(marks_dict.values())
    n = len(scores)

    if n == 0:
        return 0

    if n % 2 != 0:
        return scores[n // 2]
    else:
        return (scores[n // 2 - 1] + scores[n // 2]) / 2

def find_max_score(marks_dict):
    student = max(marks_dict, key=marks_dict.get)
    return student, marks_dict[student]

def find_min_score(marks_dict):
    student = min(marks_dict, key=marks_dict.get)
    return student, marks_dict[student]

#  GRADE ASSIGNMENT #
def assign_grades(marks_dict):
    grades = {}

    for name, score in marks_dict.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"

    return grades

def grade_distribution(grades_dict):
    dist = {"A":0, "B":0, "C":0, "D":0, "F":0}

    for g in grades_dict.values():
        dist[g] += 1

    return dist

#  PASS / FAIL  #
def pass_fail_filter(marks_dict):
    passed = [name for name, score in marks_dict.items() if score >= 40]
    failed = [name for name, score in marks_dict.items() if score < 40]
    return passed, failed

#  RESULTS TABLE  #
def print_results_table(marks_dict, grades_dict):
    print("\n FINAL RESULTS ")
    print(f"{'Name':<15}{'Marks':<10}{'Grade':<10}")
    print("-------------------------------------------------")

    for name in marks_dict:
        print(f"{name:<15}{marks_dict[name]:<10}{grades_dict[name]:<10}")

    print("-------------------------------------------------")

#  EXPORT CSV  #
def export_to_csv(marks_dict, grades_dict):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"final_results_{timestamp}.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Marks", "Grade"])

        for name in marks_dict:
            writer.writerow([name, marks_dict[name], grades_dict[name]])

    print(f"\n📁 Results exported to: {filename}")

#  MAIN LOOP  #
while True:
    show_menu()
    choice = int(input("Choose an option: "))

    if choice == 1:
        marks_dict = manual_input()

    elif choice == 2:
        marks_dict = load_from_csv()
        if len(marks_dict) == 0:
            continue  

    elif choice == 3:
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
        continue

    #  PROCESS DATA  #
    avg = calculate_average(marks_dict)
    median = calculate_median(marks_dict)
    max_student, max_score = find_max_score(marks_dict)
    min_student, min_score = find_min_score(marks_dict)

    grades_dict = assign_grades(marks_dict)
    dist = grade_distribution(grades_dict)
    passed, failed = pass_fail_filter(marks_dict)

    #  PRINT RESULTS  #
    print_results_table(marks_dict, grades_dict)

    print("\n--- STATISTICS ---")
    print(f"Average Marks: {avg:.2f}")
    print(f"Median Marks: {median}")
    print(f"Top Scorer: {max_student} ({max_score})")
    print(f"Lowest Scorer: {min_student} ({min_score})")

    print("\n--- GRADE DISTRIBUTION ---")
    for grade, count in dist.items():
        print(f"{grade}: {count}")

    print("\n--- PASS / FAIL ---")
    print(f"Passed ({len(passed)}): {passed}")
    print(f"Failed ({len(failed)}): {failed}")

    # BONUS EXPORT  #
    save = input("\nDo you want to export the results to CSV? (y/n): ").lower()
    if save == "y":
        export_to_csv(marks_dict, grades_dict)

    print("\nRun another analysis? (y/n)")
    again = input().lower()
    if again != "y":
        print("Program ended.")
        break
