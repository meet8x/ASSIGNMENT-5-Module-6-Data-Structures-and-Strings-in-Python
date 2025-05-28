student_details = {"Meet":55,"Pranay":99,"Drashti":78}

search_name = input("Enter the student's name: ")

if search_name in student_details:
    marks = student_details[search_name]
    print(f"{search_name}'s Marks: {marks}")
else:
    print("Student not found")