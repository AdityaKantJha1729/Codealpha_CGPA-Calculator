def calculate_cgpa():
    total_credits = 0
    total_grade_points = 0
    num_courses = int(input("Enter number of courses: "))

    for i in range(num_courses):
        print(f"\nCourse {i+1}:")
        grade = float(input("Enter grade (0-10): "))
        credits = int(input("Enter credit hours: "))
        total_grade_points += grade * credits
        total_credits += credits
        print(f"Grade = {grade}, Credits = {credits}")

    if total_credits == 0:
        print("No valid credits entered.")
    else:
        cgpa = total_grade_points / total_credits
        print(f"\nYour CGPA is: {cgpa:.2f}")

if __name__ == "__main__":
    calculate_cgpa()
