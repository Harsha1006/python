students_grades = {
    "Alice": [85, 90, 88],
    "Bob": [78, 82, 80],
    "Charlie": [92, 95, 91],
    "David": [70, 74, 72]
}
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0
def write_results_to_file(filename, results):
    with open(filename, 'w') as file:
        for student, avg_grade in results.items():
            file.write(f"{student}: {avg_grade:.2f}\n")
def main():
    results = {}
    
    # Calculate the average for each student
    for student, grades in students_grades.items():
        avg_grade = calculate_average(grades)
        results[student] = avg_grade
    
    # Write the results to a file
    write_results_to_file('student_averages.txt', results)
    print("Results have been written to 'student_averages.txt'.")
if __name__ == "__main__":
    main()
